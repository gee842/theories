#include <stdio.h>
#include <stdlib.h>
#include<time.h>
#include <string.h>
#include "MT.h"

#define LBOX 500
double mass[LBOX][LBOX];
double cluster[LBOX][LBOX];
double periphery[LBOX][LBOX];
double colonylist[LBOX*LBOX][4]; //index, N, periphery, netmass
double density;
double coverratio;
int totsites,totcolonies,totperi;
double CurrentTime;

//parameters from the command line
static long int Tsteps;
static double dilution;
static long int replica;

//parameters from "input.txt"
static double r,K,r_l,Nmax,gg,stopratio,layer,m0,c_mu,r_s,minT,sampling;
static int sigma;

//Internally calculated parameters.
static double A,B;

void read_input();
void set_initial();
int check_boundary(int);
void merge(int, int);
int min(int,int);
int max(int,int);
void massgrowth(double);
void reshapelist(); //this also updates totcolonies and totperi.
int getnewindex();
int issurrounded(int,int);
void expansion();
void migration();
void swimming();
void stabilitycheck();
double getnetmass();
double prop_mig(double,double);
double T_mig(double,double);

FILE* outputratio;
FILE* outputnetmass;

//program need to get Tsteps and dilution from the command line. Also, replica index for bash script.
int main(int argc, char** argv)
{
// Declare variables
	int i, index;
	char filename[50], suffix[50], buffer[50];
	double Tproceed;
	double P[3], T[3], delt[3];
	int count=0;
// Read parameters from the command line and input file.
	read_input();
	Tsteps = strtol(argv[1],NULL,10);
	dilution = strtod(argv[2],NULL);
	if(argc<=3){
		replica = 0;
	}
	else{
		replica = strtol(argv[3],NULL,10);
	}
	A = pow(10,dilution)-1.0;
	B = c_mu * LBOX * LBOX* Nmax / r_l;
	printf("Tsteps %d, dilution %.2lf \n",Tsteps,dilution);
// Setup the name of the ouput files
	strcpy(filename,"ratio_");
	sprintf(suffix, "dilution%.2lf_T%d_%d.txt", dilution,Tsteps,replica);
	strcat(filename,suffix);
	outputratio=fopen(filename,"w");
	strcpy(filename,"netmass_");
	sprintf(suffix, "dilution%.2lf_T%d_%d.txt", dilution,Tsteps,replica);
	strcat(filename,suffix);
	outputnetmass=fopen(filename,"w");

// Set initial conditions
	init_genrand((unsigned)time(NULL));
	set_initial();
	reshapelist();

	CurrentTime = 0.0;
	for(i=0;i<3;i++){
		T[i]=0.0;
		P[i]= -log(genrand_real3());
	}

// Steps with the next reaction method
	while(CurrentTime<Tsteps){
		//Calculate Delta t_k for all the processes
		// [0]:growth, [1]:swimming, [2]:migration. [3]: mass growth only.
		if(totperi==0){
			delt[0]=Tsteps;
			delt[1]=Tsteps;
		}
		else if(r_s==0.0){
			delt[0]=(P[0]-T[0])/totperi;
			delt[1]=Tsteps;
		}
		else{
			delt[0]=(P[0]-T[0])/totperi;
			delt[1]=(P[1]-T[1])/totperi/r_s;
		}
		delt[2]=prop_mig(CurrentTime,P[2]-T[2]);

		//Determine the minimum Delta t_k and the process.
		Tproceed=Tsteps;
		index=0;
		for(i=0;i<3;i++){
			if(delt[i]<Tproceed){
				index = i;
				Tproceed = delt[i];
			}
		}
		if(Tproceed>minT){
			Tproceed = minT;
			index =3;
		}

		//Update the internal time T_k for all the process.
		T[0] = T[0] + totperi*Tproceed;
		T[1] = T[1] + totperi * Tproceed * r_s;
		T[2] = T[2] + T_mig(CurrentTime, Tproceed);
		//Update the mass
		massgrowth(Tproceed);
		//Do a process and evaluate the stability
		if(index==0){
			expansion();
			P[index] = P[index]-log(genrand_real3());
		}
		else if(index==1){
			swimming();
			P[index] = P[index]-log(genrand_real3());
		}
		else if(index==2){
			migration();
			P[index] = P[index]-log(genrand_real3());
		}
		stabilitycheck();

		//Update the real time.
		CurrentTime = CurrentTime + Tproceed;

		//Caulate the coveratio. Quit if it exceeds a certain value.
		coverratio = 1.0*totsites/(LBOX*LBOX);
		//output the coveratio and netmass
		if(CurrentTime > sampling*count){
			count++;
			fprintf(outputratio,"%lf %lf \n",CurrentTime, coverratio);
			fprintf(outputnetmass,"%lf %lf \n",CurrentTime, getnetmass());
		}

		if(coverratio>stopratio){
			fprintf(outputratio,"%lf %lf \n",CurrentTime, coverratio);
			fprintf(outputnetmass,"%lf %lf \n",CurrentTime, getnetmass());
			break;
		}
	}

	fclose(outputratio);
	fclose(outputnetmass);

	return 0;
}

//read input parameters from file "input.txt"
void read_input(){
    char line[101];
    int max_length = 100;
    FILE * input_file;
    input_file = fopen("input.txt","r");
    // layer, effective ALI thickness
    fgets(line,max_length,input_file);
    sscanf(line,"%lf",&layer);
    // m0, mass for the first colonization
    fgets(line,max_length,input_file);
    sscanf(line,"%lf",&m0);
    // c_mu, migration from bulk to ALI
    fgets(line,max_length,input_file);
    sscanf(line,"%lf",&c_mu);
    // r, vertical growth rate.
    fgets(line,max_length,input_file);
    sscanf(line,"%lf",&r);
    // K, carrying capacity for the vertical growth.
    fgets(line,max_length,input_file);
    sscanf(line,"%lf",&K);
    // r_l, liquid bulk growth rate.
    fgets(line,max_length,input_file);
    sscanf(line,"%lf",&r_l);
    // Nmax, carrying capacity for the liquid bulk growth.
    fgets(line,max_length,input_file);
    sscanf(line,"%lf",&Nmax);
    // gg, coefficient for the stability check
    fgets(line,max_length,input_file);
    sscanf(line,"%lf",&gg);
    // stopratio, simulation stops if ALI is coverd by this.
    fgets(line,max_length,input_file);
    sscanf(line,"%lf",&stopratio);
    // r_s, this ratio of pheriphery cells can move to another site.
    fgets(line,max_length,input_file);
    sscanf(line,"%lf",&r_s);
    // sigma, the spreading of Gaussian dist. for swimming.
    fgets(line,max_length,input_file);
    sscanf(line,"%d",&sigma);
    // minT, the minimum time step for the vertical growth
    fgets(line,max_length,input_file);
    sscanf(line,"%lf",&minT);
    // sampling, the time interval for sampling.
    fgets(line,max_length,input_file);
    sscanf(line,"%lf",&sampling);
    fclose(input_file);
}

//initialzie variables and set initial condition.
void set_initial(){
	int k, l,ininum;
	int xrand, yrand;
	int xad, yad, currentmax;
	int new,exist,flag;

	for(k=0; k<LBOX; k++){
		for(l=0; l<LBOX; l++){
			mass[k][l]=0;
			cluster[k][l]=0;
			periphery[k][l]=0;
		}
	}
	for(k=0; k<LBOX*LBOX; k++){
		for(l=0; l<4; l++){
			colonylist[k][l]=0;
		}
	}

	density = Nmax*pow(10,-dilution);
	ininum = floor(density*LBOX*LBOX*layer*0.001);
	totsites = ininum;
	currentmax = 0;
	for(k=0; k<ininum; k++){
		l=0;
		while(l==0){
			xrand = floor(genrand_real2()*LBOX);
			yrand = floor(genrand_real2()*LBOX);
			if(mass[xrand][yrand]==0){
				// occupy a random site
				new = currentmax+1;
				mass[xrand][yrand]=m0;
				cluster[xrand][yrand]=new;
				periphery[xrand][yrand]=new;
				colonylist[currentmax][0]=new;
				colonylist[currentmax][1]=1;
				colonylist[currentmax][2]=1;
				colonylist[currentmax][3]=m0;

				// see the 4 adjacent sites. Merge if needed.
				flag = 0;
				xad = check_boundary(xrand+1);
				yad = check_boundary(yrand);
				if((cluster[xad][yad]!=0)&&(cluster[xad][yad]!=new)){
					exist = cluster[xad][yad];
					merge(exist,new);
					new = min(new,exist);
					flag++;
				}
				xad = check_boundary(xrand-1);
				yad = check_boundary(yrand);
				if((cluster[xad][yad]!=0)&&(cluster[xad][yad]!=new)){
					exist = cluster[xad][yad];
					merge(exist,new);
					new = min(new,exist);
					flag++;
				}
				xad = check_boundary(xrand);
				yad = check_boundary(yrand+1);
				if((cluster[xad][yad]!=0)&&(cluster[xad][yad]!=new)){
					exist = cluster[xad][yad];
					merge(exist,new);
					new = min(new,exist);
					flag++;
				}
				xad = check_boundary(xrand);
				yad = check_boundary(yrand-1);
				if((cluster[xad][yad]!=0)&&(cluster[xad][yad]!=new)){
					exist = cluster[xad][yad];
					merge(exist,new);
					new = min(new,exist);
					flag++;
				}

				if(flag==0){
					currentmax++;
				}

				l=1;
			}
		}
	}
}

int check_boundary(int q){
	if(q>=LBOX){
		return q-LBOX;
	}
	else if(q<0){
		return q+LBOX;
	}
	else{
		return q;
	}
}

//merge colony 1 and colony 2. Preserve the smaller index.
void merge(int col_1, int col_2){
	int k,l, index_s, index_b, xad, yad, count;
	int small = min(col_1, col_2);
	int big = max(col_1, col_2);
	int numperi = 0;

	//relabel the cluster and periphery
	for(k=0; k<LBOX; k++){
		for(l=0; l<LBOX; l++){
			//relabel index
			if(cluster[k][l]==big){
				cluster[k][l] = small;
			}
			//relabel periphery
			if(cluster[k][l]==small){
				count = 0;
				xad = check_boundary(k+1);
				yad = check_boundary(l);
				if(cluster[xad][yad]==0){
					count++;
				}
				xad = check_boundary(k-1);
				yad = check_boundary(l);
				if(cluster[xad][yad]==0){
					count++;
				}
				xad = check_boundary(k);
				yad = check_boundary(l+1);
				if(cluster[xad][yad]==0){
					count++;
				}
				xad = check_boundary(k);
				yad = check_boundary(l-1);
				if(cluster[xad][yad]==0){
					count++;
				}

				if(count==0){
					periphery[k][l]=0;
				}
				else{
					periphery[k][l]=small;
					numperi++;
				}
			}
		}
	}

	//find the indices from the colony list
	for(k=0; k<LBOX*LBOX; k++){
		if(colonylist[k][0]==small){
			index_s = k;
			break;
		}
	}
	for(k=0; k<LBOX*LBOX; k++){
		if(colonylist[k][0]==big){
			index_b = k;
			break;
		}
	}

	//update the colony list
	colonylist[index_s][1] = colonylist[index_s][1]+colonylist[index_b][1];
	colonylist[index_s][2] = numperi;
	colonylist[index_s][3] = colonylist[index_s][3]+colonylist[index_b][3];
	colonylist[index_b][0] = 0;
	colonylist[index_b][1] = 0;
	colonylist[index_b][2] = 0;
	colonylist[index_b][3] = 0;
}

// Choose one occupied site and expand the colony from the site. (Surface growth)
void expansion(){
	int siterand,k,l,index,nth,listindex;
	int site=0;
	int xsite, ysite,xad,yad,xadad,yadad,exist;
	int count=0;
	int flag=0;
	double adj[4];
	// Randomly pick a site using the colony list.
	siterand = ceil(genrand_real2()*totperi);
	for(k=0;k<totcolonies;k++){
		site = site + colonylist[k][2];
		if(site>=siterand){
			index=colonylist[k][0];
			listindex=k;
			nth = siterand - (site - colonylist[k][2]);
			break;
		}
	}
	// get XY of the site
	for(k=0;k<LBOX;k++){
		for(l=0;l<LBOX;l++){
			if(periphery[k][l]==index){
				count++;
				if(count==nth){
					xsite = k;
					ysite = l;
					flag = 1;
					break;
				}
			}
		}
		if(flag==1){
			break;
		}
	}
	// choose a new site. first see the number of empty neighbors and radomly choose one.
	for(k=0;k<4;k++){
		adj[k]=0;
	}
	count=0;
	xad = check_boundary(xsite+1);
	yad = check_boundary(ysite);
	if(cluster[xad][yad]==0){
		adj[0]=1;
		count++;
	}
	xad = check_boundary(xsite-1);
	yad = check_boundary(ysite);
	if(cluster[xad][yad]==0){
		adj[1]=1;
		count++;
	}
	xad = check_boundary(xsite);
	yad = check_boundary(ysite+1);
	if(cluster[xad][yad]==0){
		adj[2]=1;
		count++;
	}
	xad = check_boundary(xsite);
	yad = check_boundary(ysite-1);
	if(cluster[xad][yad]==0){
		adj[3]=1;
		count++;
	}
	nth =ceil(genrand_real2()*count);
	count=0;
	for(k=0;k<4;k++){
		if(adj[k]==1){
			count++;
		}
		if(count==nth){
			if(k==0){
				xad = check_boundary(xsite+1);
				yad = check_boundary(ysite);
				break;
			}
			else if(k==1){
				xad = check_boundary(xsite-1);
				yad = check_boundary(ysite);
				break;
			}
			else if(k==2){
				xad = check_boundary(xsite);
				yad = check_boundary(ysite+1);
				break;
			}
			else if(k==3){
				xad = check_boundary(xsite);
				yad = check_boundary(ysite-1);
				break;
			}
		}
	}
	//update the site. merge if needed. Note that merge func updates the periphery.
	cluster[xad][yad]=index;
	mass[xad][yad]=m0;
	colonylist[listindex][1]++;
	colonylist[listindex][3] = colonylist[listindex][3] + m0;
	totsites++;
	count=0;
	xadad = check_boundary(xad+1);
	yadad = check_boundary(yad);
	if((cluster[xadad][yadad]!=0)&&(cluster[xadad][yadad]!=index)){
		exist=cluster[xadad][yadad];
		merge(exist,index);
		index = min(index,exist);
		count++;
	}
	xadad = check_boundary(xad-1);
	yadad = check_boundary(yad);
	if((cluster[xadad][yadad]!=0)&&(cluster[xadad][yadad]!=index)){
		exist=cluster[xadad][yadad];
		merge(exist,index);
		index = min(index,exist);
		count++;
	}
	xadad = check_boundary(xad);
	yadad = check_boundary(yad+1);
	if((cluster[xadad][yadad]!=0)&&(cluster[xadad][yadad]!=index)){
		exist=cluster[xadad][yadad];
		merge(exist,index);
		index = min(index,exist);
		count++;
	}
	xadad = check_boundary(xad);
	yadad = check_boundary(yad-1);
	if((cluster[xadad][yadad]!=0)&&(cluster[xadad][yadad]!=index)){
		exist=cluster[xadad][yadad];
		merge(exist,index);
		index = min(index,exist);
		count++;
	}
	//relabel the periphery of the index, if no merge happens.
	if(count==0){
		// see the site
		if(issurrounded(xad,yad)==0){
			periphery[xad][yad]=index;
			colonylist[listindex][2]++;
		}
		// see the neighbor sites
		xadad = check_boundary(xad+1);
		yadad = check_boundary(yad);
		if((periphery[xadad][yadad]==index)&&(issurrounded(xadad,yadad)==1)){
			periphery[xadad][yadad]=0;
			colonylist[listindex][2]--;
		}
		xadad = check_boundary(xad-1);
		yadad = check_boundary(yad);
		if((periphery[xadad][yadad]==index)&&(issurrounded(xadad,yadad)==1)){
			periphery[xadad][yadad]=0;
			colonylist[listindex][2]--;
		}
		xadad = check_boundary(xad);
		yadad = check_boundary(yad+1);
		if((periphery[xadad][yadad]==index)&&(issurrounded(xadad,yadad)==1)){
			periphery[xadad][yadad]=0;
			colonylist[listindex][2]--;
		}
		xadad = check_boundary(xad);
		yadad = check_boundary(yad-1);
		if((periphery[xadad][yadad]==index)&&(issurrounded(xadad,yadad)==1)){
			periphery[xadad][yadad]=0;
			colonylist[listindex][2]--;
		}
	}
	reshapelist();
}

//return 1 if all the 4 neighbor sites are occupied. otherwise, return 0.
int issurrounded(int x, int y){
	int xad, yad;
	int count = 0;
	xad = check_boundary(x+1);
	yad = check_boundary(y);
	if(cluster[xad][yad]!=0){
		count++;
	}
	xad = check_boundary(x-1);
	yad = check_boundary(y);
	if(cluster[xad][yad]!=0){
		count++;
	}
	xad = check_boundary(x);
	yad = check_boundary(y+1);
	if(cluster[xad][yad]!=0){
		count++;
	}
	xad = check_boundary(x);
	yad = check_boundary(y-1);
	if(cluster[xad][yad]!=0){
		count++;
	}

	if(count==4){
		return 1;
	}
	else{
		return 0;
	}
}

// reshape the colony list. remove empty rows from the list.
void reshapelist(){
	int site=0;
	int index=0;
	int k,n;
	while(site<totsites){
		if(colonylist[index][0]==0){
			//insert the next non-zero component
			n=1;
			while(1){
				if(colonylist[index+n][0]!=0){
					for(k=0;k<4;k++){
						colonylist[index][k]=colonylist[index+n][k];
						colonylist[index+n][k]=0;
					}
					break;
				}
				else{
					n++;
				}
			}
		}
		else{
			site=site+colonylist[index][1];
			index++;
		}
	}
	//update totcolonies;
	for(k=0;k<totsites+1;k++){
		if(colonylist[k][0]==0){
			totcolonies=k;
			break;
		}
	}
	//update totperi;
	totperi=0;
	for(k=0;k<totcolonies;k++){
		totperi=totperi+colonylist[k][2];
	}
}

// get the smallest unused index
int getnewindex(){
	int k=0;
	int newindex=1;
	int flag;
	while(newindex<totsites+1){
		flag=1;
		for(k=0;k<totcolonies;k++){
			if(colonylist[k][0]==newindex){
				newindex++;
				flag=0;
				break;
			}
		}
		if(flag==1){
			break;
		}
	}
	return newindex;
}

//Vertical mass growth (logistic growth)
void massgrowth(double Tdelta){
	int k,l,m;
	double growth;
	for(k=0;k<LBOX;k++){
		for(l=0;l<LBOX;l++){
			if(mass[k][l]!=0){
				growth = r*(1-mass[k][l]/K)*mass[k][l]*Tdelta;
				mass[k][l]=mass[k][l]+growth;
				for(m=0;m<totcolonies;m++){
					if(colonylist[m][0]==cluster[k][l]){
						colonylist[m][3]=colonylist[m][3]+growth;
					}
				}
			}
		}
	}
}

//Migration from the bulk liquid to the air-liquid interface. Migration fails if the site is already occupied.
void migration(){
	int k, attempts,newindex, exist;
	int xrand, yrand, xad, yad;
	int flag;
	attempts = 1; //change here if you need multiple attempts.
	for(k=0;k<attempts;k++){
		xrand = floor(genrand_real2()*LBOX);
		yrand = floor(genrand_real2()*LBOX);
		if(cluster[xrand][yrand]==0){
			newindex = getnewindex();
			mass[xrand][yrand] = m0;
			cluster[xrand][yrand] = newindex;
			periphery[xrand][yrand]= newindex;
			colonylist[totcolonies][0]=newindex;
			colonylist[totcolonies][1]=1;
			colonylist[totcolonies][2]=1;
			colonylist[totcolonies][3]=m0;
			totcolonies++;
			totsites++;
			totperi++;

			//merge if there are neighbors
			flag=0;
			xad = check_boundary(xrand+1);
			yad = check_boundary(yrand);
			if((cluster[xad][yad]!=0)&&(cluster[xad][yad]!=newindex)){
				exist = cluster[xad][yad];
				merge(exist,newindex);
				newindex = min(newindex,exist);
				flag++;
			}
			xad = check_boundary(xrand-1);
			yad = check_boundary(yrand);
			if((cluster[xad][yad]!=0)&&(cluster[xad][yad]!=newindex)){
				exist = cluster[xad][yad];
				merge(exist,newindex);
				newindex = min(newindex,exist);
				flag++;
			}
			xad = check_boundary(xrand);
			yad = check_boundary(yrand+1);
			if((cluster[xad][yad]!=0)&&(cluster[xad][yad]!=newindex)){
				exist = cluster[xad][yad];
				merge(exist,newindex);
				newindex = min(newindex,exist);
				flag++;
			}
			xad = check_boundary(xrand);
			yad = check_boundary(yrand-1);
			if((cluster[xad][yad]!=0)&&(cluster[xad][yad]!=newindex)){
				exist = cluster[xad][yad];
				merge(exist,newindex);
				newindex = min(newindex,exist);
				flag++;
			}
			//if merger happens, reshape the list.
			if(flag!=0){
				reshapelist();
			}
		}
	}
}

//remove colonies if they get too heavy. Bouyancy is included in gg.
void stabilitycheck(){
	int k,x,y;
	double gravity, surfacetension;
	for(k=0;k<totcolonies;k++){
		gravity = colonylist[k][3];
		surfacetension = colonylist[k][2]*gg;
		if(gravity>surfacetension){
			totsites = totsites - colonylist[k][1];
			for(x=0;x<LBOX;x++){
				for(y=0;y<LBOX;y++){
					if(cluster[x][y]==colonylist[k][0]){
						cluster[x][y]=0;
						mass[x][y]=0;
						periphery[x][y]=0;
					}
				}
			}
			colonylist[k][0]=0;
			colonylist[k][1]=0;
			colonylist[k][2]=0;
			colonylist[k][3]=0;
		}
	}
	reshapelist(); //this also updates totcolonies and totperi
}




//swimming event. A periphery site replaces to another site.
void swimming(){
	int siterand,k,l,nth,listindex,index,newindex,exist;
	int site=0;
	int xsite, ysite, xnew, ynew, xad, yad;
	int count=0;
	int flag=0;
	double dr, d, gap,mingap;

	// draw a distance from Gaussian (generated by Box-Muller method).
	dr = fabs(genrand_BM() * sigma);
	// break if the closest site was the same positon (|dr|<0.5). = Swimming fails.
	if(dr<0.5){
		return;
	}

	// Randomly pick a site using the colony list.
	siterand = ceil(genrand_real2()*totperi);
	for(k=0;k<totcolonies;k++){
		site = site + colonylist[k][2];
		if(site>=siterand){
			index=colonylist[k][0];
			nth = siterand - (site - colonylist[k][2]);
			break;
		}
	}
	// get XY of the site
	for(k=0;k<LBOX;k++){
		for(l=0;l<LBOX;l++){
			if(periphery[k][l]==index){
				count++;
				if(count==nth){
					xsite = k;
					ysite = l;
					flag = 1;
					break;
				}
			}
		}
		if(flag==1){
			break;
		}
	}

	// choose a new site. First, draw a random distance. And scan the neighbors to list up the closest sites.
	mingap=5*sigma; //bigger than possible.
	count=0;
	for(k=0;k<6*sigma;k++){
		for(l=0;l<6*sigma;l++){
			xnew = check_boundary(xsite+k-3*sigma);
			ynew = check_boundary(ysite+l-3*sigma);
			if(mass[xnew][ynew]==0.0){
				d = sqrt(1.0*(k-3*sigma)*(k-3*sigma) + 1.0*(l-3*sigma)*(l-3*sigma));
				gap = fabs(dr-d);
				if(gap==mingap){
					count++;
				}
				else if(gap<mingap){
					count=1;
					mingap = gap;
				}
			}
		}
	}
	nth = ceil(genrand_real2()*(double)count);
	count=0;
	flag=0;
	for(k=0;k<6*sigma;k++){
		for(l=0;l<6*sigma;l++){
			xnew = check_boundary(xsite+k-3*sigma);
			ynew = check_boundary(ysite+l-3*sigma);
			if(mass[xnew][ynew]==0){
				d = sqrt(1.0*(k-3*sigma)*(k-3*sigma) + 1.0*(l-3*sigma)*(l-3*sigma));
				gap = fabs(dr-d);
				if(gap==mingap){
					count++;
					if(count==nth){
						flag=1;
						break;
					}
				}
			}
		}
		if(flag==1){
			break;
		}
	}

	//colonize (xnew,ynew). Resolve merging.
	newindex = getnewindex();
	mass[xnew][ynew]=m0;
	cluster[xnew][ynew] = newindex;
	periphery[xnew][ynew]= newindex;
	colonylist[totcolonies][0]=newindex;
	colonylist[totcolonies][1]=1;
	colonylist[totcolonies][2]=1;
	colonylist[totcolonies][3]=m0;
	totcolonies++;
	totsites++;
	totperi++;

	//merge if there are neighbors
	flag=0;
	xad = check_boundary(xnew+1);
	yad = check_boundary(ynew);
	if((cluster[xad][yad]!=0)&&(cluster[xad][yad]!=newindex)){
		exist = cluster[xad][yad];
		merge(exist,newindex);
		newindex = min(newindex,exist);
		flag++;
	}
	xad = check_boundary(xnew-1);
	yad = check_boundary(ynew);
	if((cluster[xad][yad]!=0)&&(cluster[xad][yad]!=newindex)){
		exist = cluster[xad][yad];
		merge(exist,newindex);
		newindex = min(newindex,exist);
		flag++;
	}
	xad = check_boundary(xnew);
	yad = check_boundary(ynew+1);
	if((cluster[xad][yad]!=0)&&(cluster[xad][yad]!=newindex)){
		exist = cluster[xad][yad];
		merge(exist,newindex);
		newindex = min(newindex,exist);
		flag++;
	}
	xad = check_boundary(xnew);
	yad = check_boundary(ynew-1);
	if((cluster[xad][yad]!=0)&&(cluster[xad][yad]!=newindex)){
		exist = cluster[xad][yad];
		merge(exist,newindex);
		newindex = min(newindex,exist);
		flag++;
	}
	
	//if merger happens, reshape the list.
	if(flag!=0){
		reshapelist();
	}
}







//calculate and return the current net biomass.
double getnetmass(){
	int k;
	double total=0.0;
	for(k=0;k<totcolonies;k++){
		total = total + colonylist[k][3];
	}
	return total;
}

double T_mig(double TimeNow,double TimeGap){
	return B*log((exp(r_l*(TimeNow+TimeGap))+A)/(exp(r_l*TimeNow)+A));
}

double prop_mig(double TimeNow,double alpha){
	double inlog;
	inlog = (exp(r_l*TimeNow)+A)*exp(alpha/B) - A;
	return log(inlog)/r_l - TimeNow;
}

int min(int a, int b){
	if(a<b){
		return a;
	}
	else{
		return b;
	}
}

int max(int a, int b){
	if(a>b){
		return a;
	}
	else{
		return b;
	}
}