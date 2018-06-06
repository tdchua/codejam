#include <iostream>
#include <algorithm>
using namespace std;

int main( void ) {

  int testcases = 0;
  cin >> testcases;

  int i;
  for( i = 0; i < testcases; i++ ) {

    int numbers;
    cin >> numbers;
    int j;
    int myarrayofnumbers[numbers];
    for( j = 0; j < numbers; j++ ) {
      cin >> myarrayofnumbers[j];
    }
    bool noerror = false;
    while( noerror == false ) {
      noerror = true;
      int k;
      for( k = 0; k < numbers - 2; k++ ) {
        // cout << myarrayofnumbers[k] << " " << myarrayofnumbers[k+2] << endl;
        if( myarrayofnumbers[k] > myarrayofnumbers[k+2] ) {
          swap( myarrayofnumbers[k], myarrayofnumbers[k+2] );
          noerror = false;
        }
      }
    }

    noerror = true;
    for( j = 0; j < numbers - 1; j++ ) {
      // cout << j << endl;
      int z;
      for( z = j + 1; z < numbers; z++ ) {
        if( myarrayofnumbers[j] > myarrayofnumbers[z] ) {
          noerror = false;
          break;
        }
      }
      if( noerror == false )
        break;
    }
    cout << "Case #" << i+1 << ": ";
    int f;
    // for( f = 0; f < numbers; f++ )
    //   cout << myarrayofnumbers[f] << " ";
    // cout << endl;

    if( noerror == true )
      cout << "OK" << endl;
    else
      cout << j << endl;
  }
  return 0;
}
