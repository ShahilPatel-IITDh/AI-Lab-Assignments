/*
* @file botTemplate.cpp
* @author Arun Tejasvi Chaganty <arunchaganty@gmail.com>
* @date 2010-02-04
* Template for users to create their own bots
*/

#include <chrono>
#include "Othello.h"
#include "OthelloPlayer.h"
#include "OthelloBoard.h"


using namespace std;
using namespace Desdemona;


//Define the values of INT_MIN and INT_MAX
#define INT_MIN -2147483648
#define INT_MAX +2147483647


//start time 
auto start = chrono::steady_clock::now();

class MyBot : public OthelloPlayer
{
public:
    MyBot(Turn turn);

    virtual Move play(const OthelloBoard &board);
    virtual int minMaxAlgo(OthelloBoard &board, Turn turn, int depth, Move move, int Min, int Max);
    virtual int heuristicForMinMax(OthelloBoard &board, int mode);
};

MyBot::MyBot(Turn turn) : OthelloPlayer(turn) 
{

}

Move MyBot::play(const OthelloBoard &board)
{
    start = chrono::steady_clock::now();
    list<Move> nextMoves = board.getValidMoves(turn);
    Move bestMove = *nextMoves.begin();
    int bestScore = INT_MIN, depth = 1;

    //We initialize variable depth with value 1

    while (depth++) // While 2 seconds not over || full board explored
    {
        for (Move nextMove : nextMoves)
        {
            OthelloBoard gameBoard = OthelloBoard(board);

            int Heuristic_Value;

            Heuristic_Value = minMaxAlgo(gameBoard, this->turn, depth, nextMove, INT_MIN, INT_MAX);

            if (Heuristic_Value > bestScore) //if Heuristic value is greater than best score then update the value of bestscore with value of heuristic.
            {
                bestMove = nextMove;  //update best move to the value of next move because the value of heuristic is greater than best score.
                bestScore = Heuristic_Value;
            }

            if (Heuristic_Value == INT_MIN) // Condition for checking the best move attained till the time is exhausted, i.e. when the value of heuristic reaches INT_MIN.
            {
                return bestMove;
            }
        }
    }
    return bestMove;
}

int MyBot::minMaxAlgo(OthelloBoard &board, Turn turn, int depth, Move move, int Min, int Max)
{
    if (chrono::duration_cast<chrono::milliseconds>(chrono::steady_clock::now() - start).count() > 1600)
        return INT_MIN;

    OthelloBoard gameBoard = OthelloBoard(board);
    gameBoard.makeMove(turn, move);
    list<Move> moveTree = gameBoard.getValidMoves(other(turn));

    if (depth == 0)
        {
            return heuristicForMinMax(gameBoard, 3);
        }

    int bestValue = (this->turn == turn) ? INT_MAX : INT_MIN;

    if (this->turn == turn)
    {
        for (Move move : moveTree)
        {
            bestValue = min(bestValue, minMaxAlgo(gameBoard, other(turn), depth - 1, move, Min, Max));
            if (Min >= min(Max, bestValue))
            {
                break;
            }
        }
    }
    else
    {
        for (Move move : moveTree)
        {
            bestValue = max(bestValue, minMaxAlgo(gameBoard, other(turn), depth - 1, move, Min, Max));
            if (Max <= max(bestValue, Min))
               {
                   break;
               } 
        }
    }
    return bestValue;
}

int MyBot::heuristicForMinMax(OthelloBoard &board, int mode)
{

    int Opp_Possible_Moves = board.getValidMoves(other(this->turn)).size();
    int Player_Possible_Moves = board.getValidMoves(this->turn).size();

    int Diffence_in_Moves = Player_Possible_Moves - Opp_Possible_Moves;

    switch (mode)
    {
    
        case 1:
        {
            if (this->turn == BLACK)
            {
                return (board.getBlackCount() - board.getRedCount());
            }
            return (board.getRedCount() - board.getBlackCount());
        }
        case 2:
        {
            int Player_Pos_Value = 0, Opp_Pos_Value = 0;

            //declare all the variables 
            int x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9, x_10;
            int y_0, y_1, y_2, y_3, y_4, y_5, y_6, y_7, y_8, y_9, y_10;

            x_0[] = {0, 0, 7, 7};
            y_0[] = {0, 7, 0, 7};

            for (int i = 0; i < 4; ++i)
            {
                if (board.get(x_0[i], y_0[i]) == this->turn)
                    {
                        Player_Pos_Value += 1616;
                    }

                else if (board.get(x_0[i], y_0[i]) == other(this->turn))
                    {
                        Opp_Pos_Value += 1616;
                    }
            }

            x_1[] = {1, 0, 7, 1, 0, 6, 6, 7};
            y_1[] = {0, 1, 1, 7, 6, 0, 7, 6};

            for (int i = 0; i < 8; ++i)
            {
                if (board.get(x_1[i], y_1[i]) == this->turn)
                    {
                        Player_Pos_Value -= 351;
                    }
                else if (board.get(x_1[i], y_1[i]) == other(this->turn))
                    {
                        Opp_Pos_Value -= 351;
                    }
            }

            x_2[] = {2, 0, 7, 2, 0, 5, 5, 7};
            y_2[] = {0, 2, 2, 7, 5, 0, 7, 5};

            for (int i = 0; i < 8; ++i)
            {
                if (board.get(x_2[i], y_2[i]) == this->turn)
                    {
                        Player_Pos_Value += 116;
                    }
                else if (board.get(x_2[i], y_2[i]) == other(this->turn))
                    {
                        Opp_Pos_Value += 116;
                    }
            }

            x_3[] = {3, 0, 7, 3, 0, 4, 4, 7};
            y_3[] = {0, 3, 3, 7, 4, 0, 7, 4};

            for (int i = 0; i < 8; ++i)
            {
                if (board.get(x_3[i], y_3[i]) == this->turn)
                    {
                        Player_Pos_Value += 53;
                    }
                else if (board.get(x_3[i], y_3[i]) == other(this->turn))
                    {
                        Opp_Pos_Value += 53;
                    }
            }

            x_4[] = {1, 1, 6, 6};
            y_4[] = {1, 6, 1, 6};

            for (int i = 0; i < 4; ++i)
            {
                if (board.get(x_4[i], y_4[i]) == this->turn)
                    {
                        Player_Pos_Value -= 181;
                    }
                else if (board.get(x_4[i], y_4[i]) == other(this->turn))
                    {
                        Opp_Pos_Value -= 181;
                    }
            }

             x_5[] = {2, 1, 6, 5, 1, 5, 6, 2};
             y_5[] = {1, 2, 5, 6, 5, 1, 2, 6};

            for (int i = 0; i < 8; ++i)
            {
                if (board.get(x_5[i], y_5[i]) == this->turn)
                    {
                        Player_Pos_Value -= 6;
                    }

                else if (board.get(x_5[i], y_5[i]) == other(this->turn))
                    {
                        Opp_Pos_Value -= 6;
                    }
            }

            x_6[] = {2, 1, 6, 5, 1, 5, 6, 2, 2, 2, 5, 5};
            y_6[] = {1, 2, 5, 6, 5, 1, 2, 6, 3, 4, 3, 4};

            for (int i = 0; i < 12; ++i)
            {
                if (board.get(x_6[i], y_6[i]) == this->turn)
                    {
                        Player_Pos_Value -= 6;
                    }

                else if (board.get(x_6[i], y_6[i]) == other(this->turn))
                    {
                        Opp_Pos_Value -= 6;
                    }
            }

            x_7[] = {3, 1, 6, 4, 1, 4, 6, 3};
            y_7[] = {1, 3, 4, 6, 4, 1, 3, 6};

            for (int i = 0; i < 8; ++i)
            {
                if (board.get(x_7[i], y_7[i]) == this->turn)
                    {
                        Player_Pos_Value -= 23;
                    }

                else if (board.get(x_7[i], y_7[i]) == other(this->turn))
                    {
                        Opp_Pos_Value -= 23;
                    }
            }

            x_8[] = {2, 2, 5, 5};
            y_8[] = {2, 5, 2, 5};

            for (int i = 0; i < 4; ++i)
            {
                if (board.get(x_8[i], y_8[i]) == this->turn)
                    {
                        Player_Pos_Value += 51;
                    }
                else if (board.get(x_8[i], y_8[i]) == other(this->turn))
                    {
                        Opp_Pos_Value += 51;
                    }
            }

            x_9[] = {3, 3, 4, 4};
            y_9[] = {3, 4, 3, 4};

            for (int i = 0; i < 4; ++i)
            {
                if (board.get(x_9[i], y_9[i]) == this->turn)
                    {
                        Player_Pos_Value -= 1;
                    } 

                else if (board.get(x_9[i], y_9[i]) == other(this->turn))
                    {
                        Opp_Pos_Value -= 1;
                    }
            }

            x_10[] = {3, 3, 4, 4};
            y_10[] = {2, 5, 2, 5};

            for (int i = 0; i < 4; ++i)
            {
                if (board.get(x_10[i], y_10[i]) == this->turn)
                { 
                    Player_Pos_Value += 7;
                } 
                else if (board.get(x_10[i], y_10[i]) == other(this->turn))
                {
                    Opp_Pos_Value += 7;
                }     
            }      

            return (Player_Pos_Value - Opp_Pos_Value);
        }
        case 3:
        {
            return Diffence_in_Moves;
        }
        default:
        {
            return (board.getBlackCount() - board.getRedCount());
        }
    }
}

// The following lines are _very_ important to create a bot module for Desdemona
extern "C"
{
    OthelloPlayer *createBot(Turn turn)
    {
        return new MyBot(turn);
    }

    void destroyBot(OthelloPlayer *bot)
    {
        delete bot;
    }
}
