#include <Python.h>
#include <stdio.h>
#include <stdlib.h>



/**
 * print_python_list_info - does exactly like the name suggests
 * @p: python object
 * Return: null
 */

void print_python_list_info(PyObject *p)
{
	if (PyListCheck(p))
		print("python list object found\n");
	return 0;
}
