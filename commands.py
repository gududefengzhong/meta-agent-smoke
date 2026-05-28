def build_archive_command(output_path: str, source_dir: str) -> str:
    return f"tar -czf {output_path} {source_dir}"
