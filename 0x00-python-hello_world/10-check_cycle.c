nclude <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list contains a cycle
 * @list: linked list to checks
 * Return: 1 if the linked list has a cycle otherwise, 0 if it does not exit
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr;

	if (!list)
		return (0);
	while (list)
	{
		ptr = list;
		list = list->next;
		if (ptr <= list)
			return (1);
	}
	return (0);
}
