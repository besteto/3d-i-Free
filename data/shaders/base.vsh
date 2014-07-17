attribute vec3 position;
attribute vec2 texcoord;
attribute vec3 normal;
attribute vec3 binormal;
attribute vec3 tangent;

uniform   mat4 modelView;
uniform   mat4 prjView;

varying vec2 v_tex;
varying vec3 v_light;
varying vec3 v_eye;

const vec3 light_position = vec3(0,30,0);
const vec3 eye_position   = vec3(0,0,0);

void main()
{
	 vec4 p4 = vec4(position,1) * modelView;
     vec3 pos = p4.xyz;

     mat3 normalMatrix = mat3(modelView[0].xyz,modelView[1].xyz,modelView[2].xyz);

     mat3 tbn = mat3(
                     normalize(tangent  * normalMatrix),
                     normalize(binormal * normalMatrix),
                     normalize(normal   * normalMatrix)
                     );
     v_light = normalize(light_position - pos) * tbn;
     v_eye   = normalize(eye_position   - pos) * tbn;

     v_tex   = texcoord;
     gl_Position = p4 * prjView;

}

