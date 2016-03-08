#!/bin/bash
if `test $# -ne 1`
then
    echo Syntax error: one argument needed
    exit 1
fi

grep $1 `find . | grep ".py"` 2>/dev/null
