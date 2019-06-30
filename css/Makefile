# SCSS用汎用Makefile
SASS := sass
SCSSFLAGS :=
SASSFLAGS := ${SCSSFLAGS}
#
TARGETS += ${patsubst %.scss, %.css, ${wildcard *.scss}}

.SUFFIXES : .css .scss

%.css : %.scss
	${SASS} ${SASSFLAGS} $<:$@

.PHONY: build clean

build: ${TARGETS}

clean:
	${RM} ${TARGETS}
