


git push -u origin main



ox-alpha


https://www.youtube.com/watch?v=TOWXXhn7ctY&t=777s


GLM 5.3 Flash


https://huggingface.co/zai-org/GLM-5.3-Flash



```
ollama
```


wsl

```
uv add vllm
uv sync
uv run vllm serve "zai-org/GLM-5.3-Flash"
docker model run hf.co/zai-org/GLM-5.3-Flash 
```


https://docs.vllm.ai/en/latest/cli/serve/#frontend

https://www.designveloper.com/blog/vllm-tutorial/
```
. ./.venv/bin/activate
vllm serve "zai-org/GLM-5.3-Flash" --host
python -c "import vllm; print(vllm.__version__)"

```





$ uv add vllm
Using CPython 3.13.14 interpreter at: C:\Users\russj\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe
Creating virtual environment at: .venv
Resolved 203 packages in 2.44s
error: Distribution `nccl4py==0.4.1 @ registry+https://pypi.org/simple` can't be installed because it doesn't have a source distribution or wheel for the current platform

hint: You're on Windows (`win_amd64`), but `nccl4py` (v0.4.1) only has wheels for the following platforms: `manylinux_2_24_aarch64`, `manylinux_2_24_x86_64`, `manylinux_2_28_aarch64`, `manylinux_2_28_x86_64`; consider adding "sys_platform == 'win32' and platform_machine == 'AMD64'" to `tool.uv.required-environments` to ensure uv resolves to a version with compatible wheels



https://docs.getbifrost.ai/providers/supported-providers/vllm

```
░░░░░░░░░░░░░░░░░░░░ [0/195] Installing wheels...                                                                                                              warning: Failed to hardlink files; falling back to full copy. This may lead to degraded performance.
         If the cache and target directories are on different filesystems, hardlinking may not be supported.
         If this is intentional, set `export UV_LINK_MODE=copy` or use `--link-mode=copy` to suppress this warning.
         ```