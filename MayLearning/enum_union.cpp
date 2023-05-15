#include <iostream>
void foo (); //forward declaration
void foo2 ();


void foo ()
{
	enum A { one, two, three};
	std::cout<<one<<std::endl; //export to surrounding scope
}

void foo2()
{
	union A {
			int a;
			short b; //sharing SAME memory space
			double c;
	};
	A instance ;
	instance.a = 1;
	std::cout<<"a: "<<instance.a<<" b: "<<instance.b<<" c: "<<instance.c<<std::endl; //they share the SAME mem size
	instance. b = 2;
	std::cout<<"a: "<<instance.a<<" b: "<<instance.b<<" c: "<<instance.c<<std::endl;
}
class A{
public:
	A()
	{
		a = 10;
	}
	int a;
};

void foo4(void *arg)
{
	A* a_ptr = static_cast<A *> (arg);
	std::cout<<"foo4: "<<(*a_ptr).a<<std::endl;
}

void foo4_3(A &ref) //invalid initialization of non-const reference of type ‘A&’ from an rvalue of type ‘A*’
{

}

int main ()
{
	foo();
	foo2();

	A obj ;
	foo4(&obj);
}
