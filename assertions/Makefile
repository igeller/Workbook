

all:
	cc -c -DVERBOSE splitter.c
	cc -o reduce reduce.c
	@echo now make run
	
run:
	make test-reduce
	make test-splitter
	make clean

test-reduce: reduce
	./reduce 3 7
	./reduce 7 3
	./reduce 4 2
	./reduce 2 4
	./reduce 0 4
	./reduce 4 0 
	./reduce 0 0
	./reduce -3 7
	./reduce 7 -3
	./reduce -9 -3
	
test-splitter: splitter.o
	cc -o splitter -DTEST1 test-splitter.c splitter.o
	./splitter
	cc -o splitter -DTEST2 test-splitter.c splitter.o
	./splitter
	cc -o splitter -DTEST3 test-splitter.c splitter.o
	./splitter
	cc -o splitter -DTEST4 test-splitter.c splitter.o
	./splitter
	cc -o splitter -DTEST5 test-splitter.c splitter.o
	./splitter
	cc -o splitter -DTEST6 test-splitter.c splitter.o
	./splitter
	
clean:
	-rm splitter.o
	-rm splitter
	-rm reduce

push:
	make clean
	git add *
	git commit -m ok
	# git remote add origin https://github.com/burtr/Workbook.git
	git push -u origin master
