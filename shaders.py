from miniengine import *


def simple():
    return Material(
        '''
            attribute vec3 pos;
            attribute vec2 tex;
            uniform   mat4 modelView;
            uniform   mat4 prjView;
            varying   vec3 v_pos;
            varying   vec2 v_tex;

            void main()
            {
                v_tex=tex;
                v_pos=(pos + 1.)/2.0;
                gl_Position = vec4(pos,1) * modelView * prjView;
            }
        ''',
        '''
            varying vec2 v_tex;
            varying vec3 v_pos;

            void main()
            {
                gl_FragColor = vec4(v_pos,1);
            }
        '''
    )


def cells():
    return Material(
        '''
            attribute vec3  pos;
            attribute vec2  tex;
            uniform mat4 modelView;
            uniform mat4 prjView;

            varying   vec2  v_tex;
            void main()
            {
                v_tex=tex;
                gl_Position = vec4(pos,1) * modelView * prjView;
            }
        ''',
        '''
            uniform float time;
            varying vec2  v_tex;

            void main()
            {
                float c = .1/cos((v_tex.x*32.+(time/50.)*100.));
                c += .1/cos((v_tex.y*32.+(time/50.)*100.));
                c += sin(v_tex.x*30.);

                gl_FragColor = vec4(0,c,c,1.0 );
            }

        '''
    )


def water():
    return Material(
        '''
            attribute vec3  pos;
            attribute vec2  tex;
            uniform mat4 modelView;
            uniform mat4 prjView;

            varying   vec2  v_tex;
            void main()
            {
                v_tex=tex;
                gl_Position = vec4(pos,1) * modelView * prjView;
            }
        ''',
        '''
            uniform float time;
            varying vec2  v_tex;

            #define MAX_ITER 8

            void main()
            {
	            vec2 p = v_tex * 8.0- vec2(30.0);
	            vec2 i = p;
	            float c = 1.0;
	            float inten = .05;
	            for (int n = 0; n < MAX_ITER; n++)
	            {
		            float t = time * (1.0 - (3.0 / float(n+1)));
		            i = p + vec2(cos(t - i.x) + sin(t + i.y), sin(t - i.y) + cos(t + i.x));
		            c += 1.0/length(vec2(p.x / (sin(i.x+t)/inten),p.y / (cos(i.y+t)/inten)));
	            }
	            c /= float(MAX_ITER);
	            c = 1.5-sqrt(c);
	            gl_FragColor = vec4(pow(c, 7.0)) + vec4(0.0, 0.15, 0.25, 1.0);
}
        '''
    )


def newbie():
    return Material(
        ('''
            attribute vec3 pos;
            attribute vec2 tex;
            uniform   mat4 modelView;
            uniform   mat4 prjView;
            varying   vec3 v_pos;
            varying   vec2 v_tex;
            uniform float time;

            void main()
            {
                v_tex=tex;
                v_pos=pos;
                gl_Position = vec4(pos,1) * modelView * prjView;
            }
        '''),
        '''
            varying vec2  v_tex;
            varying vec3 v_pos;
            uniform float time;

            #define rad1 0.3
            #define rad2 0.15

            void main()
            {
                if (sqrt((v_tex.x - 0.5)*(v_tex.x - 0.5) + (v_tex.y - 0.5)*(v_tex.y - 0.5)) < (abs(sin(time))-0.5))
	                {
	                gl_FragColor = vec4(0.0,sin(time),sin(time),1.0);
	                }
	            else
	                {
	                gl_FragColor = vec4(cos(time),cos(time),0.5,1.0);
	                }
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