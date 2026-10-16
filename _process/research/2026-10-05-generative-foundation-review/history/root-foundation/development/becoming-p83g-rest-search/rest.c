#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* refutation learner over lassos in Cantor order; rest = last wrong-or-silent step + 1 */
static int pi[100000], pq[100000];
static int o[200000];
int main(int argc,char**argv){
  int Nmax=atoi(argv[1]); int A=argc>2?atoi(argv[2]):2;
  int K=0; for(int d=0;d<64;d++) for(int q=0;q<=d;q++){pi[K]=d-q;pq[K]=q;K++;}
  for(int N=1;N<=Nmax;N++){
    long T=(long)N+(2L*N-1)*(N*(N+1)/2)+5; if(T>199999)T=199999;
    long best=-1; int bi=0,bq=0; int bv[64];
    for(int i=0;i<N;i++) for(int q=0;i+q+1<=N;q++){
      int L=i+q+1; long total=1; for(int j=0;j<L;j++) total*=A;
      for(long code=0;code<total;code++){
        long c=code; for(int j=0;j<L;j++){o[j]=c%A;c/=A;}
        for(long t=L;t<T;t++) o[t]=o[t-(q+1)];
        int k=0; long last=-1;
        for(long t=0;t<T;t++){
          int hi=pi[k],hq=pq[k];
          if(hi+hq+1<=t){ if(o[t-(hq+1)]!=o[t]){last=t;k++;} }
          else last=t;
        }
        if(last+1>best){best=last+1;bi=i;bq=q;for(int j=0;j<L;j++)bv[j]=o[j];}
      }
    }
    printf("%d %ld  i=%d q=%d  ",N,best,bi,bq); for(int j=0;j<bi+bq+1;j++)printf("%d",bv[j]); printf("   bound %ld\n",(long)N+(2L*N-1)*(N*(N+1)/2));
    fflush(stdout);
  }
}
