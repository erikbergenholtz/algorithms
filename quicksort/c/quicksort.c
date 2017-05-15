/*
 * quicksort.c
 * Avg:   O(n log(n))
 * Worst: O(n^2)
 */

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define LEN 10
#define MAX 100

void randomize(int *, long);
void quicksort(int *, long, long);
long partition(int *, long, long);
void print(int *, long);
void swap(int *, int *);

int main( void )
{
	srand(time(NULL));
	int arr[LEN];
	randomize(arr, LEN);
	quicksort(arr, 0, LEN-1);
	print(arr, LEN);
	return 0;
}

void randomize(int *arr, long l)
{
	for(long i=0 ; i<l ; ++i)
	{
		arr[i] = rand()%MAX;
	}
}

void quicksort(int *arr, long lo, long hi)
{
	if(lo<hi)
	{
		long p = partition(arr, lo, hi);
		quicksort(arr, lo, p-1);
		quicksort(arr, p+1, hi);
	}
}

long partition(int *arr, long lo, long hi)
{
	int p = arr[hi];
	long i = lo;
	for(long j=lo ; j<hi ; ++j)
	{
		if(arr[j] <= p) swap(&arr[i++], &arr[j]);
	}
	swap(&arr[i], &arr[hi]);
	return i;
}

void swap(int *a, int *b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void print(int *arr, long l)
{
	for(long i=0 ; i<l ; ++i)
	{
		printf("%d\n", arr[i]);
	}
}
