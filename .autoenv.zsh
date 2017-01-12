autostash PATH=$PATH:$HOME/miniconda3/bin
autostash CONDA_ENV="py35"

if [[ $PATH != *"$CONDA_ENV" ]]; then
  source activate $CONDA_ENV
fi
