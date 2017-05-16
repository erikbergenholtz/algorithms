/*
 * binheap.c
 * Binary Heap
 * Author: Erik Bergenholtz
 */

#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>



int size(int);
void insert(int, int **, int *, int *);
int extract(int **, int *);
void swap(int *, int *);
void expand(int **, int *);
void dump(int *, int, int, int);

int main()
{
	srand(time(NULL));
	int mDep = 5;
	int *heap = malloc(size(mDep)*sizeof(int));
	for(int i=0 ; i<size(mDep) ; i++) heap[i] = 0;
	int tail = 0;
	for(int i=0 ; i<50 ; ++i) insert(rand()%100, &heap, &tail, &mDep);
	dump(heap, 0, 0, mDep);
	for(int i=0 ; i<50 ; ++i) printf("%d ", extract(&heap, &tail));
	printf("\n");
	return 0;
}

int size(int depth)
{
	return pow(2.0, (double)depth)-1;
}

void insert(int value, int **heap, int *tail, int *mDep)
{
	if((*tail) >= size(*mDep)) expand(heap, mDep);
	(*heap)[*tail] = value;
	int c = (*tail)++;
	int p = (c-1)/2;
	while((*heap)[c] > (*heap)[p])
	{
		swap(&(*heap)[c],&(*heap)[p]);
		c = p;
		p = (c-1)/2;
	}
}

int extract(int **heap, int *tail)
{
	int res = (*heap)[0];
	(*heap)[0] = (*heap)[--(*tail)];
	(*heap)[*tail] = 0;
	int p = 0;
	int c1 = (p*2)+1;
	int c2 = (p*2)+2;
	while((*heap)[c1] > (*heap)[p] || (*heap)[c2] > (*heap)[p])
	{
		if((*heap)[c1] > (*heap)[c2])
		{
			swap(&(*heap)[c1],&(*heap)[p]);
			p = c1;
		}
		else
		{
			swap(&(*heap)[c2],&(*heap)[p]);
			p = c2;
		}
		c1 = (p*2)+1;
		c2 = (p*2)+2;
	}
	return res;
}

void swap(int *a, int *b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void expand(int **arr, int *mDep)
{
	int t = size(*mDep);
	(*mDep) += 2;
	(*arr) = realloc(*arr, size(*mDep)*sizeof(int));
	for(; t<size(*mDep) ; ++t) (*arr)[t] = 0;
}

void dump(int *n, int i, int d, int mDep)
{
	for(int j=0 ; j<d ; ++j) printf("    ");
	if(n[i] == 0 || i>=size(mDep))
	{
		printf("EMPTY\n");
		return;
	}
	printf("%d\n",n[i]);
	dump(n, 2*i+1, d+1, mDep);
	dump(n, 2*i+2, d+1, mDep);
}
