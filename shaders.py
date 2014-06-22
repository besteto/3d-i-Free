from miniengine import *

def simple() :
    return Material(
        '''
            attribute vec3  pos;
            attribute vec2  tex;
            uniform float time;
            varying   vec2  v_tex;
            void main()
            {
                v_tex=tex;
                gl_Position = vec4(pos * cos(time),1);
            }
        ''',
        '''
            uniform float time;
            varying vec2  v_tex;
            void main()
            {
                gl_FragColor = vec4(v_tex,sin(time*10.0),1);
            }
        '''
    )


def zebro() :
    return Material(
        '''
            attribute vec3  pos;
            attribute vec2  tex;
            varying   vec2  v_tex;
            void main()
            {
                v_tex=tex;
                gl_Position = vec4(pos,1);
            }
        ''',
        '''
            uniform float time;
            varying vec2  v_tex;
            void main()
            {
                float x = 0.5 - v_tex.x;
                float y = 0.5 - v_tex.y;
                float r = (x * x + y * y);
                float z = cos((r +  time * 0.2)/0.01);
                gl_FragColor = vec4(z,z,z,1);
           }
        '''
    )


def flag():
    return Material(
        '''
            attribute vec3  pos;
            attribute vec2  tex;
            uniform float time;
            varying   vec2  v_tex;
            varying  vec3 v_pos;
            void main()
            {
                v_tex=tex;
                v_pos = pos;
                if ((tex.x>0.3)&&(tex.x<0.8))
                    {
                    gl_Position = vec4(pos.x, pos.y-(sin(time*10.0)/10.0),pos.z,1);
                    }
                else
                    {
                    gl_Position = vec4(pos,1);
                    }
            }
        ''',
        '''
            uniform float time;
            varying vec2  v_tex;

            varying  vec3 v_pos;
            void main()
            {
                if (sqrt((v_tex.x - 0.3)*(v_tex.x - 0.3) + (v_tex.y - 0.5)*(v_tex.y - 0.5)) < 0.2)
                    {
                    gl_FragColor = vec4(1,0,0,0);
                    }
                else
                    {
                    gl_FragColor = vec4((v_pos+1.0)/2.0,1);

                    }
            }
        '''
    )
