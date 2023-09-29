FROM sphinxdoc/sphinx-latexpdf

#RUN apt-get update \
# && apt-get install --no-install-recommends --yes \
#      gcc \
# && apt-get autoremove \
# && apt-get clean \
# && rm -rf /var/lib/apt/lists/*

COPY ./fonts_free/* /usr/share/fonts/
COPY ./fonts_private/* /usr/share/fonts/

WORKDIR /docs
ADD requirements.txt /docs
RUN pip3 install -r requirements.txt
