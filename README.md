# BloodMNIST
The BloodMNIST dataset is a part of MedMNIST - a collection of 18 (12 2D and 6 3D) standardized datasets for Biomedical Image Classification.

## General characterisitcs
The BloodMNIST is based on a dataset of individual normal cells, captured from people without infection, hematologic or oncologic disease and free of any pharmacologic treatment at the moment of blood collection. It contains a total of 17,092 images and is organized into 8 classes. The source dataset is split with a ratio of 7:1:2 into training, validation and test set. The source images with resolution 3 × 360 × 363 pixels.

### Number of data points
In BloodMNIST there are three splits: **training validaion testing**

|split|train|val|test|
|---|---|---|---|
|n data|11,959|1,712|3,421

### Classes
There are 8 classes (Multiclass problem):

- 0: basophil
- 1: eosinophil
- 2: erythroblast
- 3: immature granulocytes(myelocytes, metamyelocytes and promyelocytes)
- 4: lymphocyte
- 5: monocyte
- 6: neutrophil
- 7: platelet

#### Basophil
Basophils are the least common granulocytes, constituting about 0.5 – 1% of circulating white blood cells. They contain large, basophilic cytoplasmic granules loaded with histamine, heparin, proteases, and cytokines.

![](./img/Basophile-9.jpeg)

#### Eosinophil
Eosinophils make up about 1 – 3% of circulating leukocytes, they arise in the bone marrow, then enter blood and tissues (especially the gastrointestinal tract, spleen, and thymus). Eosinophils combat multicellular parasites via degranulation and participate in allergic inflammation (e.g., asthma, atopic dermatitis).

![](./img/Eosinophil_blood_smear.JPG)

#### Erythroblasts
Erythroblasts (also called normoblasts) are nucleated precursors in the bone marrow that progress through basophilic, polychromatic, and orthochromatic stages as they synthesize hemoglobin. They have a high nucleus‑to‑cytoplasm ratio and condensing chromatin.

![https://www.cellwiki.net/en/cells/erythrocytes-erythroblast-basophile](./img/erythroblast.jpg)

#### Immature granulocytes(myelocytes, metamyelocytes and promyelocytes)
- Myelocytes follow promyelocytes, acquiring lineage‑specific secondary granules (neutrophilic, eosinophilic, or basophilic). They have a round/oval nucleus lacking nucleoli and cannot divide further. 
Wikipedia

- Metamyelocytes exhibit an indented (“kidney‑shaped”) nucleus; granule content is mature. They cannot proliferate and are the last stage before band cells and fully mature granulocytes. 

- Promyelocytes are ≈ 12–20 μm precursors with basophilic cytoplasm containing primary (azurophilic) granules; their nucleus is round with visible nucleoli. 
Wikipedia

#### Lymphocyte
Lymphocytes are a type of white blood cell (or leukocyte). They help an organism to fight infections. They occur in the immune system of all vertebrates. All lymphoctes have a large, blob-like nucleus.

![](./img/Lymphocyte2.jpg)

#### Monocytes
Monocytes are a type of white blood cell, part of the human body's immune system. They are usually identified in stained smears by their large two-lobed nuclei. They are a kind of reserve cell which turn into macrophages and immune helper cells called dendritic cells.

![](./img/Monocyte_40x.JPG)

#### Neutrophils
Neutrophils are the most common type of white blood cell, often called neutrophil granulocytes. They destroy bacteria (and other parasites like fungi) during an infection. They get to the site of an injury within minutes. They have tiny granules full of enzymes and peptides which chop up the bacteria after they have taken them in.

![](./img/20100825_023736_Neutrophil.jpg)

#### Platelet
A platelet is a cell fragment that circulates in the blood. Platelets are involved in hemostasis through the making of blood clots. A low platelet count (number of platelets in the blood) can cause a person to bleed without their blood clotting (making scabs). A high platelet count can increase the risk of thrombosis (blood clots inside blood vessels), which stops blood from flowing properly.

![](./img/Platelets.jpg)

