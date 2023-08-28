#include <iostream>
#include <string>
using namespace std;
char name[45];
class stud
{
private:
    int roll_no, clas, math, science, so_science, hindi, eng, t;

    
    char f_name[25], m_name[25], dof[15];
    float per;

public:
    void enter();
    void marks();
    void calcu();
};
void stud::enter()
{
    cout << "\nEnter your class:";
    cin >> clas;
    cout << "\nEnter your roll number:";
    cin >> roll_no;
    cout << "\nEnter your name:";
    cin>> name;
    cout << "\nEnter your father name:";
    cin >> f_name;
    cout << "\nEnter your mother name:";
    cin >> m_name;
    cout << "\nEnter your Date of birth:";
    cin >> dof;
}
void stud::marks()
{

    cout << "\nEnter your math marks:";
    cin >> math;
    cout << "\nEnter your science marks:";
    cin >> science;
    cout << "\nEnter your social science marks:";
    cin >> so_science;
    cout << "\nEnter your hindi marks:";
    cin >> hindi;
    cout << "\nEnter your english marks:";
    cin >> eng;
}
void stud::calcu()
{

    t = math + science + so_science + hindi + eng;
    per = t / 5;
    cout<<"Percentage is ="<<per<<" %"<<endl;

    if (per >= 75 && per <= 100)
    {
        cout << "\n 1st division";
    }
    else if (per >= 60 && per <= 75)
    {
        cout << "\n 2nd division";
    }
    else if (per >= 33 && per <= 60)
    {
        cout << "\n 3rd division";
    }
    else
    {
        cout << "Fail";
    }
}
int main()
{
    stud s;
    s.enter();
    s.marks();
    s.calcu();
    return 0;
}
