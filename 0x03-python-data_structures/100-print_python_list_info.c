#include <Python.h>
/**
 * print_python_list_info - prints information about python lists
 * @p: A PyObject list
 */

void print_python_list_info(PyObject *p);
{
	int y, alloc, size;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python list = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (y = 0; y < size; y++)
	{
		printf("Element %d: ", y);
		obj = PyList_Getltem(p, y);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
