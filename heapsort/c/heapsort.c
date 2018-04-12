/*
 * heapsort.c
 * Heapsort
 * Best:  O(n log(n))
 * Avg.:  O(n log(n))
 * Worst: O(n log(n))
 * Author: Erik Bergenholtz
 */

#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>

typedef struct {
	int maxDepth;
	int tail;
	int *heap;
} Heap;

int size(int);
void insert(int, Heap *);
int extract(Heap *);
void swap(int *, int *);
void expand(Heap *);
void dump(Heap *, int, int);

int main()
{
	srand(time(NULL));
	Heap h;
	h.maxDepth = 5;
	h.tail = 0;
	h.heap = malloc(size(h.maxDepth)*sizeof(int));
	for(int i=0 ; i<size(h.maxDepth) ; i++) h.heap[i] = 0;
	for(int i=0 ; i<70 ; ++i) insert((rand()%100)+1, &h);
	dump(&h, 0, 0);
	for(int i=0 ; i<70 ; ++i) printf("%d ", extract(&h));
	printf("\n");
	return 0;
}

int size(int depth)
{
	return pow(2.0, (double)depth)-1;
}

void insert(int value, Heap *heap)
{
	if((heap->tail) >= size(heap->maxDepth)) expand(heap);
	heap->heap[heap->tail] = value;
	int c = heap->tail++;
	int p = (c-1)/2;
	while(heap->heap[c] > heap->heap[p])
	{
		swap(&heap->heap[c],&heap->heap[p]);
		c = p;
		p = (c-1)/2;
	}
}

int extract(Heap *h)
{
	int res = h->heap[0];
	h->heap[0] = h->heap[--h->tail];
	h->heap[h->tail] = 0;
	int p = 0;
	int c1 = (p*2)+1;
	int c2 = (p*2)+2;
	while(h->heap[c1] > h->heap[p] || h->heap[c2] > h->heap[p])
	{
		if(h->heap[c1] > h->heap[c2])
		{
			swap(&h->heap[c1],&h->heap[p]);
			p = c1;
		}
		else
		{
			swap(&h->heap[c2],&h->heap[p]);
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

void expand(Heap *h)
{
	int t = size(h->maxDepth);
	h->maxDepth += 2;
	h->heap = realloc(h->heap, size(h->maxDepth)*sizeof(int));
	for(; t<size(h->maxDepth) ; ++t) h->heap[t] = 0;
}

void dump(Heap *h, int i, int d)
{
	for(int j=0 ; j<d ; ++j) printf("    ");
	if(h->heap[i] == 0 || i>=size(h->maxDepth))
	{
		printf("EMPTY\n");
		return;
	}
	printf("%d\n",h->heap[i]);
	dump(h, 2*i+1, d+1);
	dump(h, 2*i+2, d+1);
}
