bool isPalindrome(int x){
    char x_s[12];
    sprintf(x_s, "%d", x);

    int left = 0;
    int right = strlen(x_s)-1;

    while (left < right) {

        if (x_s[left] != x_s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}