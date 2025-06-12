public int factorial(int n) {
    // Missing base case: if (n <= 1) return 1;
    return n * factorial(n - 1);
} 