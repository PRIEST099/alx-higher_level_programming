#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a singly linked list
 * @list: list pointer
 * Return: 1 if cycle found, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *found = list;
	int a = 0;

	while (list != NULL)
	{
		if (list == found && a != 0)
			return (1);
		list = list->next;
		a++;
	}
	return (0);
}
