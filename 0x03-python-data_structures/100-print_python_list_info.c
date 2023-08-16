#include <Python.h>
#include <object.h>
#include <listobject.h>


/**
 * print_python_list_info - Prints the basic Python lists info
 * @p: PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int s, a, j;
	PyObject *obj;

	s = Py_SIZE(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", a);

	for (j = 0; j < s; j++)
	{
		printf("Element %d: ", j);

		obj = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
