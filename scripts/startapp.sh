#!/bin/bash
export DJANGO_PROJECT="./django_rest/"
${DJANGO_PROJECT}/manage.py startapp $1
mv $1 ${DJANGO_PROJECT}/