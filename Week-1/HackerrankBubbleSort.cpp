void countSwaps(vector<int> a) {
    int counter = 0;
    for (int i = 0; i < a.size(); i++) {

    for (int j = 0; j < a.size() - 1; j++) {
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            counter++;
        }
    }
}
    cout<< "Array is sorted in " << counter << " swaps." << endl ;
    cout << "First Element: " << a[0] << endl;
    cout << "Last Element: " << a[a.size()-1] << endl;
}
