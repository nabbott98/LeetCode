function isPalindrome(x: number): boolean {
    var rev = 0, xCopy = x; // creating variables for reversed integer and a copy for x
    while (xCopy > 0) { rev = rev * 10 + xCopy % 10; xCopy = Math.floor(xCopy/10); } // I did xCopy > 0 instead of xCopy != 0 so that it excludes negative integers
    return (rev == x && xCopy > -1); // Returns true only when rev is equal to x AND xCopy isn't negative
};