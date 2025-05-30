from visualize_attention import visualize_vit_attention

for label in range(9):
    for ex in range(10):

        visualize_vit_attention(
            model_path='./PathMNIST_ViT/checkpoint-3520',
            model_name='google/vit-base-patch16-224',
            label_idx=label,
            data_idx=ex,
            device='cuda:0',
            output_path=f'img/attention/attention_heatmap_{label}-{ex}.png',
            overlay_path=f'img/attention/attention_overlay_{label}-{ex}.png',
            alpha=0.4,
            reduce='all',  # 'mean', 'max', or 'all'
            head=0       # specify head index to override reduce
        )