// demo.cpp : Defines the exported functions for the DLL application.
//

#include "stdafx.h"

#ifdef _DEBUG
#define _DEBUG_WAS_DEFINED 1
#undef _DEBUG
#endif // _DEBUG

#include "Python.h"

#ifdef _DEBUG_WAS_DEFINED
#define _DEBUG 1
#endif // _DEBUG_WAS_DEFINED

static PyObject *
demo_function(PyObject *self, PyObject *args)
{
    double i;

    if (!PyArg_ParseTuple(args, "d", &i))
    {
        return NULL;
    }

    //return PyLong_FromLong(i + 1);
    return PyFloat_FromDouble(i + 1);
}

static PyMethodDef DemoMethods[] =
{
    { "add_one",  demo_function, METH_VARARGS, "A C function to add one to the number." },
    { NULL, NULL, 0, NULL }        /* Sentinel */
};

static struct PyModuleDef demo_module = {
    PyModuleDef_HEAD_INIT,
    "demo",             /* name of module */
    "a demo module",    /* module documentation, may be NULL */
    -1,                 /* size of per-interpreter state of the module,
                        or -1 if the module keeps state in global variables. */
    DemoMethods
};

PyMODINIT_FUNC
PyInit_demo(void)
{
    return PyModule_Create(&demo_module);
}
