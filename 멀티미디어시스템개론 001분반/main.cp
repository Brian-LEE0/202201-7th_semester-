#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include <vector>
#include <iostream>
#include <cmath>
using namespace std;
using namespace cv;
bool use_mask;
const char* image_window = "Source Image";
int match_method;
vector<float> C(8,1);

int max_Trackbar = 5;
float _2dDCTBasis[8][8][8][8];
void ImgtoDCT(Mat img,Mat& DCT, vector<float> C);
void DCTtoImg_lossy(Mat DCT,Mat& img, vector<float> C, int lossy);
void set2DBasis();


int main( int argc, char** argv )
{
    C[0] = 1/sqrt(2);
    for(int i=0; i<8;i++){
        cout << C[i] <<endl;
    }
    set2DBasis();
    cout <<argv[0]<<endl;
    string image_name = "test5.jpeg";
    Mat img = imread( image_name, IMREAD_COLOR );
    if(img.empty()){
        return -1;
    }
    Mat DCT(Size(img.cols,img.rows),CV_32FC1);
    Mat img_g(Size(img.cols,img.rows),CV_8UC1);
    Mat img_g8x8(Size(img.cols,img.rows),CV_8UC1);
    Mat img_g4x4(Size(img.cols,img.rows),CV_8UC1);
    Mat img_g2x2(Size(img.cols,img.rows),CV_8UC1);
    cvtColor(img, img_g, COLOR_RGB2GRAY );
    imshow(image_window,img_g);
    //waitKey(0);
    ImgtoDCT(img_g,DCT,C);
    DCTtoImg_lossy(DCT,img_g8x8,C,8);
    DCTtoImg_lossy(DCT,img_g4x4,C,4);
    DCTtoImg_lossy(DCT,img_g2x2,C,2);
    imshow("8x8",img_g8x8);
    imshow("4x4",img_g4x4);
    imshow("2x2",img_g2x2);
    waitKey(0);
    return 0;
    
}

void set2DBasis(){
    for (int u = 0; u < 8; u++) {
        for(int v =0; v < 8; v++){
            for(int i =0; i < 8; i++){
                for(int j =0; j < 8; j++){
                    float a,b,c;
                    a = C[u]*C[v]/4;
                    b = cos((2*i+1)*u*M_PI/16);
                    c = cos((2*j+1)*v*M_PI/16);
                    _2dDCTBasis[v][u][j][i] = a*b*c;
                    
                }
            }
            
        }
    }
    
    for (int a = 0; a<8; a++) {
        cout << "u = " << a << endl;
        for (int b = 0; b<8; b++) {
            for (int c = 0; c<8; c++) {
                cout << _2dDCTBasis[0][a][b][c] << " ";
            }
            cout << endl;
        }
    }
}

void ImgtoDCT(Mat img,Mat& DCT, vector<float> C)
{
    for (int k = 0; k < img.rows/8; k++) {
        for(int l =0; l < img.cols/8; l++){
            for(int v =0; v < 8; v++) {
                for (int u = 0; u < 8; u++){
                    float sum = 0;
                    for(int j =0; j < 8; j++){
                        for(int i =0; i < 8; i++){
                            sum+=img.at<uchar>(k*8+i,l*8+j)*_2dDCTBasis[v][u][j][i];
                        }
                    }
                    DCT.at<float>(k*8+u,l*8+v)=sum;
                    
                }
            }
            
        }
    }
    //imshow("",DCT);
    //waitKey(0);
    
    return;
}

void DCTtoImg_lossy(Mat DCT,Mat& img, vector<float> C, int lossy)
{
    for (int k = 0; k < img.rows/8; k++) {
        for(int l =0; l < img.cols/8; l++){
            for(int j =0; j < 8; j++){
                for(int i =0; i < 8; i++){
                    float sum = 0;
                    for(int v =0; v < lossy; v++){
                        for(int u =0; u < lossy; u++){
                            sum+=DCT.at<float>(k*8+u,l*8+v)*_2dDCTBasis[v][u][j][i];
                        }
                    }
                    img.at<uchar>(k*8+i,l*8+j)=sum;
                }
            }
            
        }
    }
    return;
}
