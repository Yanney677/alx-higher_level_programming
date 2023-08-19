#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints the bytes info of python
 *
 * @p: object of python
 * Return: always 0 on success
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int s, j, lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	s = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", s);
	printf("  trying string: %s\n", str);

	if (s >= 10)
		lim = 10;
	else
		lim = s + 1;

	printf("  first %ld bytes:", lim);

	for (j = 0; j < lim; j++)
		if (str[j] >= 0)
			printf(" %02x", str[j]);
		else
			printf(" %02x", 256 + str[j]);

	printf("\n");
}

/**
 * print_python_list - print the list of python
 *
 * @p: object of python
 * Return: always 0 on success
 */
void print_python_list(PyObject *p)
{
	long int s, j;
	PyListObject *lst;
	PyObject *obj;

	s = ((PyVarObject *)(p))->ob_size;
	lst = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", lst->allocated);

	for (j = 0; j < s; j++)
	{
		obj = ((PyListObject *)p)->ob_item[j];
		printf("Element %ld: %s\n", j, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
