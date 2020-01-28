import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation

def swap(A,i,j):
	if i!=j:
		A[i], A[j]=A[j], A[i]


def BubbleSort(A):
	if len(A)==1:
		return
	
	swapped=True
	for i in range(len(A)-1):
		if not swapped:
			break
		swapped=False
		for j in range(len(A)-i-1):
			if A[j]>A[j+1]:
				swap(A,j,j+1)
				swapped=True
		yield A

def Selection(A):
	if len(A)==1:
		return

	for i in range(len(A)):
		min_value=A[i]
		index=i
		for j in range(i,len(A)):
			if A[j]<min_value:
				min_value = A[j]
				index = j
			yield A
		swap(A,i,index)
		yield A



def quicksort(A,start,end):

	if start>=end:
		return
	
	if start<end:
		pivot=A[end]
		pindex=start
		for i in range(start,end):
			if A[i]<pivot:
				swap(A,i,pindex)
				pindex+=1
			yield A
		swap(A,pindex,end)
		yield from quicksort(A,start,pindex-1)
		yield from quicksort(A,pindex+1,end)




if __name__=='__main__':

	N=int(input("Enter the range for sorting: "))
	A = [x + 1 for x in range(N)]
	random.shuffle(A)
	msg=input("Enter the Sorting Algorithm's first character \n1.bubble\n2.selection\n3.quicksort\n")
	if msg == 'b':
		title = "BubbleSort"
		generator = BubbleSort(A)
	elif msg == 's':
		title = "SelectionSort"
		generator = Selection(A)
	else:
		title = "QuickSort"
		generator = quicksort(A,0,N-1)
	fig, ax = plt.subplots()
	ax.set_title(title)
	#ax.bar returns container which has all other bar rectangles
	bars = ax.bar(range(len(A)), A, align="edge")

	#Set limits of x and y axis
	ax.set_xlim(0, N)
	ax.set_ylim(0, int(1.07 * N))

	#Coordinates are the fraction of axes not data coordinates
	text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
	iteration = [0]
	def update_fig(A, rects, iteration):
		for rect, val in zip(rects, A):
			rect.set_height(val)			#To set heights of bar rectangles
		iteration[0] += 1
		text.set_text(f"# of operations: {iteration[0]}")

	#fun is to call a function recursively with fargs as additional arguements
	anim = animation.FuncAnimation(fig, func=update_fig,fargs=(bars, iteration), frames=generator, interval=1,repeat=False)
	plt.show()

	
