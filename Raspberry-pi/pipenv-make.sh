#!/bin/bash
pip freeze > pip_env.txt
touch pip_env_tmp.txt
grep -v '^numpy' pip_env.txt > pip_env_tmp.txt
mv pip_env_tmp.txt pip_env.txt
echo "numpy" >> pip_env.txt