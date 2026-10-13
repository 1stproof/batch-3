FROM ubuntu@sha256:008173c23f95b170204355c12626cb5a965d779a7e1283b09e9cffbb1bf33ca3
ARG TARGETARCH
ENV DEBIAN_FRONTEND=noninteractive
RUN timeout 300 apt-get -o Acquire::Retries=0 -o Acquire::http::Timeout=30 update && \
    timeout 900 apt-get -o Acquire::Retries=0 -o Acquire::http::Timeout=30 install -y --no-install-recommends \
    ca-certificates curl git build-essential zstd unzip xz-utils perl libseccomp2 procps \
    python3 python3-venv python3-dev latexmk texlive-latex-base texlive-latex-recommended \
    texlive-latex-extra texlive-fonts-recommended texlive-science texlive-pictures texlive-xetex texlive-luatex poppler-utils && \
    rm -rf /var/lib/apt/lists/*
COPY deployment/batch3/release-lock.json deployment/batch3/requirements.lock deployment/batch3/install_tools.py /opt/environment/
RUN timeout 1500 python3 /opt/environment/install_tools.py "$TARGETARCH"
RUN python3 -m venv /opt/python && timeout 600 /opt/python/bin/pip install --no-cache-dir --retries 0 --timeout 30 -r /opt/environment/requirements.lock
ENV PATH="/opt/python/bin:/opt/lean/bin:/usr/local/bin:/usr/bin:/bin"
RUN mkdir /opt/mathlib && cd /opt/mathlib && git init && git remote add origin https://github.com/leanprover-community/mathlib4.git && \
    timeout 300 git fetch --depth=1 origin 1fe0a51a5ecdee23c424b6e29ecb1d40eb35316d && git checkout --detach FETCH_HEAD && \
    test "$(cat lean-toolchain)" = "leanprover/lean4:v4.34.0-rc1"
WORKDIR /opt/mathlib
# Set readable cache permissions in the producing layer to avoid copying the
# entire Mathlib library into a second Docker layer.
RUN timeout 1500 lake exe cache get && lake env printenv LEAN_PATH > /opt/environment/lean-path.txt && \
    git diff --exit-code -- lake-manifest.json lakefile.lean lean-toolchain && \
    chmod -R a+rX /opt/mathlib
COPY deployment/batch3/configure_environment.py /opt/environment/
RUN python /opt/environment/configure_environment.py
ENV PATH="/opt/python/bin:/usr/local/bin:/opt/lean/bin:/usr/bin:/bin"
COPY deployment/batch3/smoke /opt/environment/smoke
RUN lake env lean /opt/environment/smoke/MathlibSmoke.lean
WORKDIR /opt/environment/smoke
RUN python scientific.py && latexmk -pdf -no-shell-escape -interaction=nonstopmode -halt-on-error tools.tex && \
    xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error tools.tex && \
    lualatex -no-shell-escape -interaction=nonstopmode -halt-on-error tools.tex && pdfinfo tools.pdf
COPY src /opt/merlean/src
COPY workflows /opt/merlean/workflows
COPY roles /opt/merlean/roles
COPY ports /opt/merlean/ports
COPY docs /opt/merlean/docs
COPY scripts /opt/merlean/scripts
COPY tests /opt/merlean/tests
COPY assets /opt/merlean/assets
COPY templates /opt/merlean/templates
COPY examples /opt/merlean/examples
COPY plugins /opt/merlean/plugins
COPY deployment/batch3 /opt/merlean/deployment/batch3
COPY Dockerfile hardware.json /opt/merlean/
COPY AGENTS.md README.md LICENSE NOTICE PRIVACY.md SECURITY.md SUPPORT.md TERMS.md /opt/merlean/
RUN /usr/sbin/useradd --create-home --uid 10001 --shell /bin/bash runner
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /opt/merlean
CMD ["/opt/python/bin/python", "-B", "/opt/merlean/src/batch3_submission.py"]
