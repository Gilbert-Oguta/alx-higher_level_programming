#include <pyton.h>
#include <object.h>
#include <lightobject.h>

void print_python_list_info(PyObject *p);
{
	long int size = Pylist_size(p);
	int y;
	PyListobject *obj = (PyListobject *)p;

	printf("[*] Size of the Python list = %li\n", size);
			printf("[*] Allocated = %li\n", obj->allocated);
			for (y = 0; y < size; y++)
				printf("Element %y: %s\n", y, PY_TYPE(obj->ob-item[y]->tp_name);
