from sglang.test.doc_patch import launch_server_cmd
from sglang.utils import wait_for_server, terminate_process

# This is equivalent to running the following command in your terminal
# python3 -m sglang.launch_server --model-path qwen/qwen2.5-0.5b-instruct --host 0.0.0.0

server_process, port = launch_server_cmd(
    """
python3 -m sglang.launch_server --model-path qwen/qwen2.5-0.5b-instruct \
 --host 0.0.0.0 --log-level warning
"""
)

wait_for_server(f"http://localhost:{port}")


# $ uv add sglang
# Using CPython 3.13.14 interpreter at: C:\Users\russj\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe
# Creating virtual environment at: .venv
# Resolved 180 packages in 2.82s
# error: Distribution `nvidia-cutlass-dsl==4.3.5 @ registry+https://pypi.org/simple` can't be installed because it doesn't have a source distribution or wheel for the current platform

# hint: You're on Windows (`win_amd64`), but `nvidia-cutlass-dsl` (v4.3.5) only has wheels for the following platforms: `manylinux_2_28_aarch64`, `manylinux_2_28_x86_64`; consider adding "sys_platform == 'win32' and platform_machine == 'AMD64'" to `tool.uv.required-environments` to ensure uv resolves to a version with compatible wheels



# https://github.com/ggml-org/llama.cpp