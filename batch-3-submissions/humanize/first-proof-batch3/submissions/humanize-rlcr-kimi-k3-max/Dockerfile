FROM node:22-bookworm-slim

ARG CODEX_VERSION=0.157.1
ARG HUMANIZE_COMMIT=fc0e0bec143cad1ff3325b2b4d17cc2722827028

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bash \
        ca-certificates \
        coreutils \
        curl \
        findutils \
        git \
        grep \
        jq \
        latexmk \
        poppler-utils \
        python3 \
        sed \
        texlive-fonts-recommended \
        texlive-latex-base \
        texlive-latex-extra \
        texlive-latex-recommended \
        texlive-pictures \
        texlive-science \
        tini \
    && npm install --global "@openai/codex@${CODEX_VERSION}" \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /root/.npm

COPY src/patch_humanize.py /tmp/patch_humanize.py

RUN git clone https://github.com/PolyArch/humanize.git /opt/humanize \
    && git -C /opt/humanize checkout --detach "${HUMANIZE_COMMIT}" \
    && python3 /tmp/patch_humanize.py /opt/humanize \
    && test "$(git -C /opt/humanize rev-parse HEAD)" = "${HUMANIZE_COMMIT}"

WORKDIR /app
COPY src/ /app/src/
COPY tests/ /app/tests/

RUN python3 -m unittest discover -s /app/tests -v \
    && latexmk -v \
    && pdflatex --version \
    && pdfinfo -v \
    && codex --version

ENTRYPOINT ["/usr/bin/tini", "-g", "--"]
CMD ["python3", "/app/src/run.py"]
