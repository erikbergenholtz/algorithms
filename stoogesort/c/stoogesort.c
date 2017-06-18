/*
 * stoogesort.c
 * Avg.:  O(n^(log(3)/log(1.5)))
 * Worst: O(n^(log(3)/log(1.5)))
 * Author: Erik Bergenholtz
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 10

void stooge(int *, size_t, size_t);
void swap(int *, int *);
void print(int *, size_t);

int main(int argc, char ** argv)
{
	srand(time(NULL));
	int arr[N];
	for(size_t i=0 ; i<N ; ++i)
	{
		arr[i] = rand()%100;
	}
	print(arr, N);
	stooge(arr,0,N-1);
	print(arr, N);
}

void stooge(int *arr, size_t l, size_t h)
{
	if(arr[l]<arr[h]) swap(&arr[l], &arr[h]);
	if(h-l+1 > 2)
	{
		size_t t = (h-l+1)/3;
		stooge(arr, l, h-t);
		stooge(arr, l+t, h);
		stooge(arr, l, h-t);
	}
}

void swap(int *a, int *b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void print(int *arr, size_t n)
{
	for(size_t i=0 ; i<n ; ++i)
	{
		printf("%d ",arr[i]);
	}
	printf("\n");
}
