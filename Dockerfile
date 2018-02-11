# Use python runtime as the parent image
FROM python:3.6-alpine

# Set install path and working directory
ENV INSTALL_PATH /cryptobot
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

# Copy contents of the current directory into the install path
COPY . .

# Install app dependencies
RUN apk add --no-cache --virtual .build-deps \
  build-base postgresql-dev libffi-dev \
    && pip install -r config/requirements/development.txt \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver"]
