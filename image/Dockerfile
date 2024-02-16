FROM sphinxdoc/sphinx-latexpdf

RUN apt-get update \
 && apt-get install --no-install-recommends --yes \
      pandoc plantuml ghostscript \
 && apt-get autoremove \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY ./fonts_free/* /usr/share/fonts/
COPY ./fonts_private/* /usr/share/fonts/
# COPY plantuml-1.2023.11.jar /usr/share/plantuml/plantuml.jar
COPY plantuml-1.2024.3.jar /usr/share/plantuml/plantuml.jar


WORKDIR /docs
ADD requirements.txt /docs
RUN pip3 install -r requirements.txt
