uniform sampler2D texture0;
uniform sampler2D texture1;
uniform float time;

varying vec2 v_tex;
varying vec3 v_norm;
varying vec3 v_light;
varying vec3 v_eye;

const float specular_power = 10.0;

void main()
{
    vec4 col = texture2D(texture0,v_tex);

    float half_sin_time = abs(sin(time))/2.0;

    col.a = 1.0;

    if ((v_tex.y < half_sin_time) || ((1.0 - v_tex.y) < half_sin_time))
        {
        col.a = 0.1;
        }

    gl_FragColor = col;

}