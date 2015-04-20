//---------------------------------------------------------------

//Program:Maintaining Student Database using File I/O Operation
//Authors:Rakesh Shetty,Sagar M Ayi,Ramesh Sidaray Mudalagi

//---------------------------------------------------------------

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

typedef struct 
{
    int dd;
    int mm;
    int yy;
}dob;
	
typedef struct 
{
	char name[20];
	char usn[10];
	dob db;
	char adr[50];
}student;
 
//listrec() Function is used to list the Records in the File
void listrec(student std)
{
   	FILE *fp;
	fp=fopen("stdbase.dat","rb+");
        //student std;
	if(fp==NULL)
	{
	   printf("Cannot open a file\n");
	   exit(0);
	}	

	printf("Student details are as follows\n");
    printf("\nName\t\tUSN\t\tDate of Birth\t\tAddress\n");
    printf("-------------------------------------------------------------------------------------------\n");
    while(fread(&std,sizeof(std),1,fp)==1)
      printf("%s\t\t%s\t\t%d/%d/%d\t\t%s\n",std.name,std.usn,std.db.dd,std.db.mm,std.db.yy,std.adr);

    fclose(fp);

}

//writerec() function is used to Add the record to the contents to File
void writerec(student std)
{
	FILE *fp;

	fp=fopen("stdbase.dat","ab+");
	if(fp==NULL)
	{
	   printf("Cannot open a file\n");
	   exit(0);
	}
	fwrite(&std,sizeof(std),1,fp);
	
    fclose(fp);
}

//modifyrec() Function is used to modify the existing contents of the file
void modifyrec(char *argv,student std1)
{
    FILE *fp;
    int flag=1;
    student std;
	fp=fopen("stdbase.dat","rb+");

	if(fp==NULL)
	{
	   printf("Cannot open a file\n");
	   exit(0);
	}	
	fflush(stdin);
	rewind(fp);
    
    while(fread(&std,sizeof(std),1,fp)==1)
    {
    	if(strcmp(std.usn,argv)==0)
    	{
    	  flag=0;
    	  fseek(fp,-sizeof(std),SEEK_CUR);
          fwrite(&std1,sizeof(std1),1,fp);
        
	    }
	    
    }
    if(flag==1)
    	printf("Requested USN Not found");
    else
    	printf("Modified");
   	
   	fclose(fp);
}

//delerec() function is used to delete the particular record of the file
void delerec(char *argv)
{
    FILE *fp,*ft;
    int flag=1;
    student std;
	fp=fopen("stdbase.dat","rb+");
	if(fp==NULL)
	{
	   printf("Cannot open a file\n");
	   exit(0);
	}
	ft=fopen("temp.dat","wb+");
	if(fp==NULL)
	{
	   printf("Cannot open a file\n");
	   exit(0);
	}

    rewind(fp);

	while(fread(&std,sizeof(std),1,fp)==1)
	{
		if(strcmp(std.usn,argv)!=0)
		{
			
			fwrite(&std,sizeof(std),1,ft);
		}

	}

	rewind(fp);
	while(fread(&std,sizeof(std),1,fp)==1)
	{
		if(strcmp(std.usn,argv)==0)
		{
			
			flag=0;
		}

	}	

	
	fclose(ft);
	fclose(fp);
	system("rm stdbase.dat");
	system("mv temp.dat stdbase.dat");
	
	if(flag==0)
 		printf("Deleted successfuly");
    else
    	printf("Enter the correct USN");
	
	
	
}

//searchrec() Function is used to search the particular record in the file
void Searchrec(char *argv)
{
	FILE *fp;
	int flag=1;
        student std;
	
	fp=fopen("stdbase.dat","rb+");

	if(fp==NULL)
	{
		printf("cannot open a file\n");
		exit(0);
	}

	rewind(fp);
	printf("\nYour requested Search is:\n");
	printf("\nName\t\tUSN\t\tDate of Birth\t\tPlace\n");
	printf("----------------------------------------------------------------------------------------------------------\n");
	
	while(fread(&std,sizeof(std),1,fp))
	{
	    if((strstr(std.usn,argv)))
	    {
	    	flag=0;
			printf("%s\t\t%s\t\t%d/%d/%d\t\t%s\n",std.name,std.usn,std.db.dd,std.db.mm,std.db.yy,std.adr);
	    }

		else if((strstr(std.name,argv)))
		{
			flag=0;
      		printf("%s\t\t%s\t\t%d/%d/%d\t\t%s\n",std.name,std.usn,std.db.dd,std.db.mm,std.db.yy,std.adr);
		}

		else if((strstr(std.adr,argv)))
		{
			flag=0;
			printf("%s\t\t%s\t\t%d/%d/%d\t\t%s\n",std.name,std.usn,std.db.dd,std.db.mm,std.db.yy,std.adr);
		}
	    
	}
	if(flag==1)
		printf("Not Found");
	
	fclose(fp);

}

//convert() function is used to convert string(Date of Birth) to integer
int convert(char *s)
{
    int num=0,i=0;
    while(s[i])
    {
       num=num*10+s[i]-'0';
       i++;
    }
    return (num);
}

//main() function
int main(int argc, char *argv[])
{
    student std,std1;

        if(!strcmp(argv[1],"-a")) //'-a(command line argument) is for add a record'
        {
    		    strcpy(std.name,argv[2]);
    		    strcpy(std.usn,argv[3]);
    		    std.db.dd=convert(argv[4]);
    		    std.db.mm=convert(argv[5]);
    		    std.db.yy=convert(argv[6]);
    		 	strcpy(std.adr,argv[7]);
    		 	writerec(std);
        }
        else if(!strcmp(argv[1],"-l"))  //'-l(command line argument) is for list a records'
    	    listrec(std);
    	   		
    	else if(!strcmp(argv[1],"-m")) ////'-m(command line argument) is for modify a particular record' 
    	{
    	        
                strcpy(std1.name,argv[3]);
    		    strcpy(std1.usn,argv[4]);
    		 	std1.db.dd=convert(argv[5]);
    		    std1.db.mm=convert(argv[6]);
    		    std1.db.yy=convert(argv[7]);
    		 	strcpy(std1.adr,argv[8]);
				modifyrec(argv[2],std1);
	    }
    	 else if(!strcmp(argv[1],"-d"))  //'-d(command line argument) is for delete a particular record'

    	    delerec(argv[2]);
    	      
        else if(!strcmp(argv[1],"-s"))  //'-s(command line argument) is for search a  particular record'
    	    Searchrec(argv[2]);
    
    return (0);

}
