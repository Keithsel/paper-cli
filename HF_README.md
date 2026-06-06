---
license: cc-by-4.0
pretty_name: AI Conference & Journal Papers
configs:
  - config_name: acl
    data_files:
      - split: "2025"
        path: browse/acl/2025.parquet
  - config_name: cvpr
    data_files:
      - split: "2025"
        path: browse/cvpr/2025.parquet
      - split: "2024"
        path: browse/cvpr/2024.parquet
  - config_name: emnlp
    data_files:
      - split: "2025"
        path: browse/emnlp/2025.parquet
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
  - config_name: icml
    data_files:
      - split: "2025"
        path: browse/icml/2025.parquet
  - config_name: naacl
    data_files:
      - split: "2025"
        path: browse/naacl/2025.parquet
  - config_name: neurips
    data_files:
      - split: "2025"
        path: browse/neurips/2025.parquet
      - split: "2024"
        path: browse/neurips/2024.parquet
  - config_name: wacv
    data_files:
      - split: "2025"
        path: browse/wacv/2025.parquet
      - split: "2024"
        path: browse/wacv/2024.parquet
---

# AI Conference & Journal Papers

Searchable metadata for papers from top AI venues (NeurIPS, ICML, ICLR, CVPR, ICCV, WACV, ACL, EMNLP, NAACL).

- `papers.parquet`: the full dataset (all fields, all venues).
- Per-venue browse views: pick a venue in **Subset**, a year in **Split**.

Built with [papercli](https://github.com/Keithsel/papercli).