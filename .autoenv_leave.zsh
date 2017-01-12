autostash CONDA_ENV="py35"

if [[ $PATH != *"$CONDA_ENV" ]]; then
  source deactivate
fi
