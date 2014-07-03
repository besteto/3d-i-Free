uniform sampler2D texture0;
uniform sampler2D texture1;
uniform float time;

varying vec2 v_tex;
varying vec2 v_blurTexCoords[8];
varying vec3 v_norm;
varying vec3 v_light;
varying vec3 v_eye;


const float specular_power = 10.0;

void main()
{
    vec4 col = texture2D(texture0,v_tex);
   	float lambert_factor = max(dot(v_norm,v_light),0.);
    float phong_factor   = pow(max(dot(v_norm,normalize(v_light + v_eye)), 0.),specular_power);


    col += texture2D(texture0, v_blurTexCoords[ 0]);
    col += texture2D(texture0, v_blurTexCoords[ 1]);
    col += texture2D(texture0, v_blurTexCoords[ 2]);
    col += texture2D(texture0, v_blurTexCoords[ 3]);
    col += texture2D(texture0, v_blurTexCoords[ 4]);
    col += texture2D(texture0, v_blurTexCoords[ 5]);
    col += texture2D(texture0, v_blurTexCoords[ 6]);
    col += texture2D(texture0, v_blurTexCoords[ 7]);
    col += texture2D(texture0, v_tex         );

    col /= 9.;

    //col *= lambert_factor;
    //col += phong_factor;

    col.a = 1.;

    gl_FragColor = col;

}
