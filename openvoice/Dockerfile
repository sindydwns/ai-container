FROM ubuntu:latest

# install sdk
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update -y
RUN apt install -y git vim sudo curl gcc make dumb-init

# install python with specific version
RUN apt install -y build-essential libssl-dev zlib1g-dev libncurses5-dev \
    libbz2-dev libreadline-dev libsqlite3-dev libncursesw5-dev \
    xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
RUN curl https://pyenv.run | bash
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc; \
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc; \
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
RUN /root/.pyenv/bin/pyenv install 3.9.19
RUN /root/.pyenv/bin/pyenv global 3.9.19
ENV PATH /root/.pyenv/versions/3.9.19/bin:$PATH

# install packages for app
RUN apt install -y wget unzip ffmpeg jupyter
RUN pip install --upgrade pip
RUN pip install setuptools
RUN pip install torch torchvision torchaudio
RUN pip install ipykernel
RUN python -m ipykernel install --user --name=project
RUN pip install unidic
RUN python -m unidic download
RUN pip install git+https://github.com/myshell-ai/MeloTTS.git
RUN wget https://myshell-public-repo-host.s3.amazonaws.com/openvoice/checkpoints_v2_0417.zip
RUN git clone https://github.com/myshell-ai/OpenVoice.git OpenVoice
RUN pip install -r OpenVoice/requirements.txt
RUN pip install botocore==1.34.88 cached_path==1.6.2
RUN pip install ./OpenVoice

WORKDIR /app
COPY . .

# COPY install.sh .
# RUN chmod +x install.sh && /bin/sh install.sh
# ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["/usr/bin/dumb-init", "--", "sleep", "infinity"]
