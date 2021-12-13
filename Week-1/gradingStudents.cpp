vector<int> gradingStudents(vector<int> grades) {
float tmp;
for (int i = 0; i < grades.size(); ++i) {
    if (grades[i] >= 38) {
        tmp = (float)grades[i]/5 - grades[i]/5;
        if( tmp >= (float) 0.5) {
            grades[i] = (grades[i]/5 +1)*5;
        }
    }
}
return grades;
}
