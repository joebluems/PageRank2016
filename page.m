### load the H matrix ####
load H.mat
[num,teams,losses,games] = textread("teams",'%d %s %s %s','delimiter','|');

### prepare matrix for power method ####
n=length(H);
rowsumvector=ones(1,n)*H';
nonzerorows=find(rowsumvector);
zerorows=setdiff(1:n,nonzerorows);
a=sparse(zerorows,ones(1,1),ones(1,1),n,1);

#### set initial ranks and other parameters ####
residual=1;
epsilon=0.0001;
pi=ones(1,n)/n;
alpha=0.90;

### executes the power method ####
while(residual >= epsilon)
  prevpi=pi;
  pi=alpha*pi*H + (alpha*(pi*a)+1-alpha)*((1/n)*ones(1,n));
  residual=norm(pi-prevpi,1);
end

### sort by rank and print out top 25 teams ####
[B,index]=sort(pi','descend');
for i = 1:25
  printf('(%d) %s %sG %sL\n',i,teams{index(i)},games{index(i)},losses{index(i)})
endfor

