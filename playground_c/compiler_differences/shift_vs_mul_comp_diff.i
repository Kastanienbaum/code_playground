# 1 "shift_vs_mul_comp_diff.c"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "shift_vs_mul_comp_diff.c"
# 1 "C:/Users/Kartoffel/Documents/Elektronik/CodeBlocks/MinGW/lib/gcc/mingw32/4.9.2/include/stdint.h" 1 3 4
# 9 "C:/Users/Kartoffel/Documents/Elektronik/CodeBlocks/MinGW/lib/gcc/mingw32/4.9.2/include/stdint.h" 3 4
# 1 "C:/Users/Kartoffel/Documents/Elektronik/CodeBlocks/MinGW/include/stdint.h" 1 3 4
# 24 "C:/Users/Kartoffel/Documents/Elektronik/CodeBlocks/MinGW/include/stdint.h" 3 4
# 1 "C:/Users/Kartoffel/Documents/Elektronik/CodeBlocks/MinGW/lib/gcc/mingw32/4.9.2/include/stddef.h" 1 3 4
# 324 "C:/Users/Kartoffel/Documents/Elektronik/CodeBlocks/MinGW/lib/gcc/mingw32/4.9.2/include/stddef.h" 3 4
typedef short unsigned int wchar_t;
# 353 "C:/Users/Kartoffel/Documents/Elektronik/CodeBlocks/MinGW/lib/gcc/mingw32/4.9.2/include/stddef.h" 3 4
typedef short unsigned int wint_t;
# 25 "C:/Users/Kartoffel/Documents/Elektronik/CodeBlocks/MinGW/include/stdint.h" 2 3 4


typedef signed char int8_t;
typedef unsigned char uint8_t;
typedef short int16_t;
typedef unsigned short uint16_t;
typedef int int32_t;
typedef unsigned uint32_t;
typedef long long int64_t;
typedef unsigned long long uint64_t;


typedef signed char int_least8_t;
typedef unsigned char uint_least8_t;
typedef short int_least16_t;
typedef unsigned short uint_least16_t;
typedef int int_least32_t;
typedef unsigned uint_least32_t;
typedef long long int_least64_t;
typedef unsigned long long uint_least64_t;





typedef signed char int_fast8_t;
typedef unsigned char uint_fast8_t;
typedef short int_fast16_t;
typedef unsigned short uint_fast16_t;
typedef int int_fast32_t;
typedef unsigned int uint_fast32_t;
typedef long long int_fast64_t;
typedef unsigned long long uint_fast64_t;
# 66 "C:/Users/Kartoffel/Documents/Elektronik/CodeBlocks/MinGW/include/stdint.h" 3 4
  typedef int intptr_t;
# 75 "C:/Users/Kartoffel/Documents/Elektronik/CodeBlocks/MinGW/include/stdint.h" 3 4
  typedef unsigned int uintptr_t;




typedef long long intmax_t;
typedef unsigned long long uintmax_t;
# 10 "C:/Users/Kartoffel/Documents/Elektronik/CodeBlocks/MinGW/lib/gcc/mingw32/4.9.2/include/stdint.h" 2 3 4
# 2 "shift_vs_mul_comp_diff.c" 2

int main(void)
{
 uint64_t a = 42;

 a = a*2;
 a = a<<1;

 return 0;
}
