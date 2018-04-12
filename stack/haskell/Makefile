HS=ghc
HSFLAGS=--make

all: stack

stack: stack.hs
	${HS} ${HSFLAGS} $<

clean:
	rm -f *.txt *.hi *.o stack
