AWS_REGISTRY = "public.ecr.aws/j1r0q0g6/notebooks"

# list of public images
JUPYTER_WEB_APP_IMAGE = f"{AWS_REGISTRY}/jupyter-web-app"
TENSORBOARDS_WEB_APP_IMAGE = f"{AWS_REGISTRY}/tensorboards-web-app"
VOLUMES_WEB_APP_IMAGE = f"{AWS_REGISTRY}/volumes-web-app"
CENTRAL_DASHBOARD_IMAGE = f"{AWS_REGISTRY}/central-dashboard"

ADMISSION_WEBHOOK_IMAGE = f"{AWS_REGISTRY}/admission-webhook"
ACCESS_MANAGEMENT_IMAGE = f"{AWS_REGISTRY}/access-management"

PROFILE_CONTROLLER_IMAGE = f"{AWS_REGISTRY}/profile-controller"
NOTEBOOK_CONTROLLER_IMAGE = f"{AWS_REGISTRY}/notebook-controller"
TENSORBOARD_CONTROLLER_IMAGE = f"{AWS_REGISTRY}/tensorboard-controller"

NOTEBOOK_SERVER_BASE = f"{AWS_REGISTRY}/notebook-servers/base"
NOTEBOOK_SERVER_JUPYTER = f"{AWS_REGISTRY}/notebook-servers/jupyter"
NOTEBOOK_SERVER_RSTUDIO = f"{AWS_REGISTRY}/notebook-servers/rstudio"
NOTEBOOK_SERVER_CODESERVER = f"{AWS_REGISTRY}/notebook-servers/codeserver"
NOTEBOOK_SERVER_JUPYTER_PYTORCH = (
    f"{AWS_REGISTRY}/notebook-servers/jupyter-pytorch"
)

NOTEBOOK_SERVER_JUPYTER_PYTORCH_CUDA = (
    f"{AWS_REGISTRY}/notebook-servers/jupyter-pytorch-cuda"
)

NOTEBOOK_SERVER_JUPYTER_TENSORFLOW = (
    f"{AWS_REGISTRY}/notebook-servers/jupyter-tensorflow"
)

NOTEBOOK_SERVER_JUPYTER_TENSORFLOW_CUDA = (
    f"{AWS_REGISTRY}/notebook-servers/jupyter-tensorflow-cuda"
)

NOTEBOOK_SERVER_JUPYTER_PYTORCH_FULL = (
    f"{AWS_REGISTRY}/notebook-servers/jupyter-pytorch-full"
)

NOTEBOOK_SERVER_JUPYTER_PYTORCH_CUDA_FULL = (
    f"{AWS_REGISTRY}/notebook-servers/jupyter-pytorch-cuda-full"
)

NOTEBOOK_SERVER_JUPYTER_TENSORFLOW_FULL = (
    f"{AWS_REGISTRY}/notebook-servers/jupyter-tensorflow-full"
)

NOTEBOOK_SERVER_JUPYTER_TENSORFLOW_CUDA_FULL = (
    f"{AWS_REGISTRY}/notebook-servers/jupyter-tensorflow-cuda-full"
)

NOTEBOOK_SERVER_JUPYTER_SCIPY = (
    f"{AWS_REGISTRY}/notebook-servers/jupyter-scipy"
)

NOTEBOOK_SERVER_CODESERVER_PYTHON = (
    f"{AWS_REGISTRY}/notebook-servers/codeserver-python"
)

NOTEBOOK_SERVER_RSTUDIO_TIDYVERSE = (
    f"{AWS_REGISTRY}/notebook-servers/rstudio-tidyverse"
)

NOTEBOOK_SERVER_JUPYTER_PYSPARK = (
    f"{AWS_REGISTRY}/notebook-servers/jupyter-pyspark"
)
