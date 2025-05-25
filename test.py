import torch
import matplotlib.pyplot as plt
import numpy as np
from torchvision.transforms import Resize
from torchvision.transforms.functional import to_pil_image
from transformers import ViTImageProcessor, ViTForImageClassification
from dataset import GetMedMNIST
from torch.utils.data import DataLoader
from PIL import Image


def visualize_vit_attention(
    model_path: str,
    model_name: str,
    dataset_name: str = 'PathMNIST',
    split: str = 'test',
    image_size: int = 224,
    batch_size: int = 1,
    device: str = 'cuda:0',
    output_path: str = 'attention_heatmap.png',
    overlay_path: str = 'attention_overlay.png',
    alpha: float = 0.6,
    reduce: str = 'mean',  # 'mean', 'max', or 'all'
    head: int = None
):

    processor = ViTImageProcessor.from_pretrained(model_name)
    model = ViTForImageClassification.from_pretrained(
        model_path,
        output_attentions=True,
        attn_implementation='eager'
    ).to(device)
    model.eval()

    dataset = GetMedMNIST(name=dataset_name, split=split, size=image_size, hf=False)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=False)

    images, _ = next(iter(loader))
    image = images[0]

    resized_image = Resize((image_size, image_size))(image)
    inputs = processor(images=resized_image, return_tensors='pt', do_rescale=False)
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)
        attentions = outputs.attentions  # List of (batch, heads, tokens, tokens)

    last_attn = attentions[-1][0]  # [num_heads, tokens, tokens]
    cls_attn = last_attn[:, 0, 1:]   # [num_heads, num_patches]
    num_heads, num_patches = cls_attn.shape
    grid_size = int(np.sqrt(num_patches))
    cls_attn = cls_attn.reshape(num_heads, grid_size, grid_size)

    def process_heatmap(hm:
        np.ndarray
    ) -> np.ndarray:
        hm = hm - hm.min()
        if hm.max() > 0:
            hm = hm / hm.max()
        return hm

    if head is not None and 0 <= head < num_heads:
        head_indices = [head]
        title_fmt = 'Head{}'
    elif reduce == 'all':
        head_indices = list(range(num_heads))
        title_fmt = 'Head{}'
    else:
        head_indices = None  # will aggregate

    if head_indices is None:
        if reduce == 'max':
            heatmap = process_heatmap(cls_attn.max(axis=0)[0].cpu().numpy())
            title = 'Max Attention'
        else:
            heatmap = process_heatmap(cls_attn.mean(axis=0).cpu().numpy())
            title = 'Mean Attention'
        _save_single(resized_image, heatmap, image_size, alpha, output_path, overlay_path)
    else:
        for i in head_indices:
            hm = process_heatmap(cls_attn[i].cpu().numpy())
            title = title_fmt.format(i)
            out_hm = output_path.replace('.', f'_head{i}.')
            out_ov = overlay_path.replace('.', f'_head{i}.')
            _save_single(resized_image, hm, image_size, alpha, out_hm, out_ov)


def _save_single(resized_image, heatmap, image_size, alpha, heatmap_path, overlay_path):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.imshow(heatmap, cmap='jet')
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(heatmap_path)
    plt.close(fig)

    hm_img = Image.fromarray(np.uint8(heatmap * 255), mode='L')
    hm_resized = hm_img.resize((image_size, image_size), resample=Image.BILINEAR)
    cmap = plt.get_cmap('jet')
    colored = cmap(np.array(hm_resized) / 255.0)[:, :, :3]
    orig = np.array(to_pil_image(resized_image)) / 255.0
    if orig.ndim == 2:
        orig = np.stack([orig]*3, axis=-1)
    overlay = (1 - alpha) * orig + alpha * colored
    overlay = np.clip(overlay, 0, 1)
    overlay_pil = Image.fromarray(np.uint8(overlay * 255))
    overlay_pil.save(overlay_path)
    print(f"Saved heatmap to {heatmap_path} and overlay to {overlay_path}")


if __name__ == '__main__':
    visualize_vit_attention(
        model_path='./PathMNIST_ViT/checkpoint-3520',
        model_name='google/vit-base-patch16-224',
        dataset_name='PathMNIST',
        split='test',
        image_size=224,
        batch_size=1,
        device='cuda:0',
        output_path='attention_heatmap.png',
        overlay_path='attention_overlay.png',
        alpha=0.6,
        reduce='all',  # 'mean', 'max', or 'all'
        head=11       # specify head index to override reduce
    )
