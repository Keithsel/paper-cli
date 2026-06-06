---
license: cc-by-4.0
pretty_name: AI Conference & Journal Papers
configs:
  - config_name: acl
    data_files:
      - split: "2025"
        path: browse/acl/2025.parquet
      - split: "2024"
        path: browse/acl/2024.parquet
      - split: "2023"
        path: browse/acl/2023.parquet
  - config_name: cvpr
    data_files:
      - split: "2026"
        path: browse/cvpr/2026.parquet
      - split: "2025"
        path: browse/cvpr/2025.parquet
      - split: "2024"
        path: browse/cvpr/2024.parquet
      - split: "2023"
        path: browse/cvpr/2023.parquet
  - config_name: emnlp
    data_files:
      - split: "2025"
        path: browse/emnlp/2025.parquet
      - split: "2024"
        path: browse/emnlp/2024.parquet
      - split: "2023"
        path: browse/emnlp/2023.parquet
  - config_name: iccv
    data_files:
      - split: "2025"
        path: browse/iccv/2025.parquet
      - split: "2023"
        path: browse/iccv/2023.parquet
  - config_name: iclr
    data_files:
      - split: "2026"
        path: browse/iclr/2026.parquet
      - split: "2025"
        path: browse/iclr/2025.parquet
      - split: "2024"
        path: browse/iclr/2024.parquet
      - split: "2023"
        path: browse/iclr/2023.parquet
  - config_name: icml
    data_files:
      - split: "2025"
        path: browse/icml/2025.parquet
      - split: "2024"
        path: browse/icml/2024.parquet
      - split: "2023"
        path: browse/icml/2023.parquet
  - config_name: ijcai
    data_files:
      - split: "2025"
        path: browse/ijcai/2025.parquet
      - split: "2024"
        path: browse/ijcai/2024.parquet
      - split: "2023"
        path: browse/ijcai/2023.parquet
  - config_name: jmlr
    data_files:
      - split: "2025"
        path: browse/jmlr/2025.parquet
      - split: "2024"
        path: browse/jmlr/2024.parquet
      - split: "2023"
        path: browse/jmlr/2023.parquet
      - split: "2022"
        path: browse/jmlr/2022.parquet
  - config_name: naacl
    data_files:
      - split: "2025"
        path: browse/naacl/2025.parquet
      - split: "2024"
        path: browse/naacl/2024.parquet
  - config_name: neurips
    data_files:
      - split: "2025"
        path: browse/neurips/2025.parquet
      - split: "2024"
        path: browse/neurips/2024.parquet
      - split: "2023"
        path: browse/neurips/2023.parquet
  - config_name: wacv
    data_files:
      - split: "2026"
        path: browse/wacv/2026.parquet
      - split: "2025"
        path: browse/wacv/2025.parquet
      - split: "2024"
        path: browse/wacv/2024.parquet
      - split: "2023"
        path: browse/wacv/2023.parquet
---

# AI Conference & Journal Papers

Searchable metadata for papers from top AI venues (NeurIPS, ICML, ICLR, CVPR, ICCV, WACV, ACL, EMNLP, NAACL).

- `papers.parquet`: the full dataset (all fields, all venues).
- Per-venue browse views: pick a venue in **Subset**, a year in **Split**.

Built with [papercli](https://github.com/Keithsel/papercli).